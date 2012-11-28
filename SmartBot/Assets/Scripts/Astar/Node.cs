using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class Node : MonoBehaviour
{
    public Vector3 m_position;
    public List<Node> m_AdjacentNodes;      /* TODO: replace with accessors */
    public List<Edge> m_ConnectedEdges;

    public bool m_useFourAdjacents = true;
    public bool m_useOverlapSphereForAdjacents = true;
    public float m_offset = 32;
    public bool m_walkable = true;
    public bool m_open, m_closed;

    public Node m_Parent;

    /* F = G + H*/
    public float m_FCost, m_GCost, m_HCost;                   /* TODO: replace with accessors */

    //flag
    public enum FlagType
    {
        FT_Door,
        FT_Cover,
        FT_Choice,
        FT_None
    }
    public FlagType m_flagtype;

    public FlagType Flag
    {
        get
        {
            return m_flagtype;
        }
    }

    public enum NodeType
    {
        NT_Door,
        NT_Cover,
        NT_Target
    }
    NodeType m_nodeType;

    public NodeType Type
    {
        get
        {
            return m_nodeType;
        }
    }

    void Awake()
    {
        Initialise();
    }

    public Node(Vector3 position, NodeType type)
    {
        m_position = position;
        m_nodeType = type;
        m_walkable = true;
        m_AdjacentNodes = new List<Node>();
        m_ConnectedEdges = new List<Edge>();
        m_FCost = m_GCost = m_HCost = 0;
        m_open = m_closed = false;
    }

    public void Initialise()
    {
        if (m_AdjacentNodes == null)
            m_AdjacentNodes = new List<Node>();
        else
            m_AdjacentNodes.Clear();
        if (m_ConnectedEdges == null)
            m_ConnectedEdges = new List<Edge>();
        else
            m_ConnectedEdges.Clear();

        m_position = transform.position;
        m_walkable = true;
        //Get adjacents
        if (m_useOverlapSphereForAdjacents)
        {
            m_AdjacentNodes.Clear();

            Collider[] adjacents;
            if (!m_useFourAdjacents)
                adjacents = Physics.OverlapSphere(m_position, m_offset * 1.4f, (1 << 9));
            else
                adjacents = Physics.OverlapSphere(m_position, m_offset * 1.1f, (1 << 9));
            foreach (Collider node in adjacents)
            {
                if (node.gameObject != gameObject)
                {
                    m_AdjacentNodes.Add(node.gameObject.GetComponent<Node>());
                }
            }
        }
        m_FCost = m_GCost = m_HCost = 0;
        m_open = m_closed = false;

        //get object at node, door, cover, etc.
        Collider[] objects = Physics.OverlapSphere(m_position, 4);
        foreach (Collider obj in objects)
        {
            switch (obj.gameObject.tag)
            {
                case "Door":
                    m_flagtype = FlagType.FT_Door;
                    break;
                case "Cover":
                    m_flagtype = FlagType.FT_Cover;
                    break;
                case "Choice":
                    m_flagtype = FlagType.FT_Choice;
                    break;
                default:
                    m_flagtype = FlagType.FT_None;
                    break;
            }
        }
    }

    //astar methods
    public void CalculateLocalFGH(Node goalNode)
    {
        bool canContinue = true;
        if (m_Parent == null)
        {
            Debug.LogError("Can't calculate FGH's, No Parent");
            canContinue = false;
        }
        if (goalNode == null)
        {
            Debug.LogError("Can't calculate FGH's, No goal");
            canContinue = false;
        }
        if (canContinue)
        {
            //calc g
            m_GCost = m_Parent.m_GCost + (m_Parent.m_position - m_position).magnitude;
            //calc h
            m_HCost = (m_position - goalNode.m_position).magnitude;
            //calc f
            m_FCost = m_GCost + m_HCost;
            MonoBehaviour.Instantiate(Resources.Load("Prefabs/AstarSearchMarker", typeof(GameObject)), m_position, Quaternion.identity);
        }
    }

    public void CalculateEdgeBasedLocalFGH(Node goalNode, float edgeCost)
    {
        bool canContinue = true;
        if (m_Parent == null)
        {
            Debug.LogError("Can't calculate FGH's, No Parent");
            canContinue = false;
        }
        if (goalNode == null)
        {
            Debug.LogError("Can't calculate FGH's, No goal");
            canContinue = false;
        }
        if (canContinue)
        {
            //calc g
            m_GCost = m_Parent.m_GCost + edgeCost;
            //calc h
            m_HCost = (m_position - goalNode.m_position).magnitude + edgeCost;  //TODO: remove magnitudes
            //calc f
            m_FCost = m_GCost + m_HCost;
        }
    }
    //~astar methods



}
