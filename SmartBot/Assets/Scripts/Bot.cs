using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class Bot : MonoBehaviour
{
    //pathfinding members
    Path m_path;
    Vector3 m_targetPosition, m_currentPosition, m_lastPosition, m_direction;

    public float m_rotationRate = 7.5f;
    public float m_moveSpeed;
    int m_nodeProximity;
    int m_currNode;

    //~pathfinding members

    public Vector3 AC_Position
    {
        get
        {
            return m_currentPosition;
        }
    }
    public Vector3 AC_Velocity
    {
        get
        {
            return m_direction * m_moveSpeed;
        }
    }

    //Current target of the controller
    public Vector3 AC_TargetPosition
    {
        get
        {
            return m_targetPosition;
        }
    }

    bool m_canMove;
    public bool AC_Move
    {
        get
        {
            return m_canMove;
        }
        set
        {
            m_canMove = value;
        }
    }

    public bool AC_Path
    {
        get
        {
            if (m_path == null)
                return false;
            else
                return true;
        }
    }
    public bool AC_PathComplete
    {
        get
        {
            if (m_currNode >= m_path.Nodes.Count)
            {
                return true;
            }
            else
                return false;
        }
    }

    Ray m_ray;
    RaycastHit m_hit;

    Vector3 m_LastLook;
    Quaternion m_targetRotation;

    Graph m_graph;
    Astar m_astar;
    Path m_graphPath;

    int m_currAction;
    bool planned = false;
    bool started = false;
    public Transform m_firepoint;

    void Awake()
    {
        m_targetPosition = transform.position;
        m_currentPosition = transform.position;

        m_nodeProximity = 1;
        m_currNode = 0;
        m_direction = new Vector3();
        m_LastLook = new Vector3();
        m_targetRotation = new Quaternion();

        m_path = Pather.PathVia;
        m_canMove = true;
        m_ray = new Ray();
        m_hit = new RaycastHit();

        m_graph = new Graph(Physics.OverlapSphere(new Vector3(720, 0, 736), 96));
        m_astar = new Astar();
        m_graphPath = new Path();

        m_currAction = 0;
    }

    public void Update()
    {
        m_path = Pather.PathVia;
        transform.position = m_currentPosition;

        m_ray = Camera.main.ScreenPointToRay(Input.mousePosition);
        if (Input.GetMouseButtonDown(1))
        {
            if (Physics.Raycast(m_ray, out m_hit, 10000, (1 << 9)))
            {
                Pather.m_start = GetClosestNode();
                Pather.m_end = m_hit.transform.GetComponent<Node>();
                m_currNode = 0;
                Pather.ComputePath();
            }
        }
        if (Input.GetKeyDown(KeyCode.C))
        {
            started = true;
        }
        if(started)
        {
            m_graph.ClearGraph();
            m_graph = new Graph(Physics.OverlapSphere(new Vector3(720, 0, 736), 96));
            GraphNode start = new GraphNode();
            GraphNode end = new GraphNode();
            foreach (GraphNode gnode in m_graph.GraphNodes)
            {
                if (gnode.Type == GraphNode.NodeType.NT_Door)
                    start = gnode;
                if (gnode.Type == GraphNode.NodeType.NT_Target)
                    end = gnode;
                if (start.m_AdjacentNodes != null && end.m_AdjacentNodes != null)
                    if (start.Type == GraphNode.NodeType.NT_Door && end.Type == GraphNode.NodeType.NT_Target)
                        break;
            }
            m_graphPath = m_astar.CalculateEdgeBasedPath(start, end);
            planned = true;
            m_currNode = 0;
            m_currAction = 0;
            started = false;
        }
        if (planned)
            ExecutePlan();
        if (m_canMove)
        {
            MoveAlongPath();
        }
        if (m_LastLook != Vector3.zero && m_LastLook - m_currentPosition != Vector3.zero)
            m_targetRotation = Quaternion.LookRotation((m_LastLook) - m_currentPosition, Vector3.up);

        if (m_lastPosition != m_currentPosition)
            animation.Play("Walk");
        else
            animation.Stop("Walk");

        transform.rotation = Quaternion.Slerp(transform.rotation, m_targetRotation, m_rotationRate * Time.deltaTime);
        m_lastPosition = m_currentPosition;
    }

    void MoveAlongPath()
    {
        //TODO: implement local avoidance
        //move
        if (m_path != null)
        {
            if (m_path.Nodes.Count > 0)
            {
                if (m_currNode < m_path.Nodes.Count)
                {
                    m_direction = (m_path.Nodes[m_currNode].transform.position - m_currentPosition).normalized;

                    LookAtPosition(m_currentPosition + m_direction);

                    m_currentPosition += m_direction * m_moveSpeed * Time.deltaTime;

                    if ((m_path.Nodes[m_currNode].transform.position - m_currentPosition).magnitude < m_nodeProximity)
                    {
                        m_currNode++;
                    }
                }
            }
        }
    }

    public void LookAtPosition(Vector3 position)
    {
        m_LastLook = new Vector3(position.x, m_currentPosition.y, position.z);
    }

    Node GetClosestNode()
    {
        float offset = GameObject.FindGameObjectWithTag("Node").GetComponent<Node>().m_offset;
        Collider[] nodes = Physics.OverlapSphere(m_currentPosition, offset, (1 << 9));
        Collider closest = nodes[0];
        foreach (Collider node in nodes)
        {
            if ((node.transform.position - m_currentPosition).magnitude < (closest.transform.position - m_currentPosition).magnitude)
                closest = node;
        }
        return closest.GetComponent<Node>();
    }

    void ExecutePlan()
    {

        if (m_graphPath != null)
        {
            if (m_graphPath.GraphNodes.Count > 0)
            {
                if (m_currNode < m_graphPath.GraphNodes.Count)
                {
                    if (m_currAction < m_graphPath.Edges.Count)
                    {
                        switch (m_graphPath.Edges[m_currAction].Action)
                        {
                            case Edge.EdgeAction.EA_Move:
                                m_direction = (m_graphPath.GraphNodes[m_currNode].m_position - m_currentPosition).normalized;

                                LookAtPosition(m_currentPosition + m_direction);

                                m_currentPosition += m_direction * m_moveSpeed * Time.deltaTime;

                                if ((m_graphPath.GraphNodes[m_currNode].m_position - m_currentPosition).magnitude < m_nodeProximity)
                                {
                                    if (m_currNode > 0)
                                        m_currAction++;
                                    m_currNode++;
                                }
                                break;
                            case Edge.EdgeAction.EA_Shoot:
                                RaycastHit hit;
                                m_direction = (m_graphPath.GraphNodes[m_currNode].m_position - m_currentPosition).normalized;
                                LookAtPosition(m_currentPosition + m_direction);
                                if (Physics.Raycast(m_firepoint.position, (new Vector3(m_graphPath.GraphNodes[m_currNode].m_position.x, 16, m_graphPath.GraphNodes[m_currNode].m_position.z) - m_firepoint.position), out hit, (new Vector3(m_graphPath.GraphNodes[m_currNode].m_position.x, 16, m_graphPath.GraphNodes[m_currNode].m_position.z) - m_firepoint.position).magnitude * 1.1f, (1 << 13)))
                                {
                                    hit.transform.gameObject.GetComponent<CombatDummy>().m_health = 0;
                                    if (m_currNode > 0)
                                        m_currAction++;
                                    m_currNode++;
                                }
                                break;
                        }
                    }
                    else
                    {
                        planned = false;
                        started = true;
                    }
                }
            }
        }
    }
}
