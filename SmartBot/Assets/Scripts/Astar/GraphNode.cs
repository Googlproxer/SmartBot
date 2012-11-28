using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class GraphNode
{
    public Vector3 m_position;
    public List<GraphNode> m_AdjacentNodes;      /* TODO: replace with accessors */
    public List<Edge> m_ConnectedEdges;

    public bool m_useFourAdjacents = true;
    public bool m_useOverlapSphereForAdjacents = true;
    public float m_offset = 32;
    public bool m_walkable = true;
    public bool m_open, m_closed;

    public GraphNode m_Parent;
    public Edge m_ParentEdge;

    /* F = G + H*/
    public float m_FCost, m_GCost, m_HCost;                   /* TODO: replace with accessors */

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

    public GraphNode()
    {
    
    }

    public GraphNode(Vector3 position, NodeType type)
    {
        m_position = position;
        m_nodeType = type;
        m_walkable = true;
        m_AdjacentNodes = new List<GraphNode>();
        m_ConnectedEdges = new List<Edge>();
        m_FCost = m_GCost = m_HCost = 0;
        m_open = m_closed = false;
    }

    public void CalculateEdgeBasedLocalFGH(GraphNode goalNode, float edgeCost)
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
