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
        return Physics.OverlapSphere(m_currentPosition, GameObject.FindGameObjectWithTag("Node").GetComponent<Node>().m_offset, (1 << 9))[0].GetComponent<Node>();
    }

    void DoCombat()
    {

    }

    void ChoosePath()
    {
        
    }
}
