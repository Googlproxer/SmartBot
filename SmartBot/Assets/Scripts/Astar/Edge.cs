using UnityEngine;
using System.Collections;

public class Edge
{
    public GraphNode m_NodeOne, m_NodeTwo;
    public GraphNode NodeOne
    {
        get
        {
            return m_NodeOne;
        }
    }
    public GraphNode NodeTwo
    {
        get
        {
            return m_NodeTwo;
        }
    }

    public float m_traversalCost;

    public Vector3 m_position;

    public enum EdgeAction
    {
        EA_Shoot,
        EA_Move
    }
    EdgeAction m_edgeAction;

    public EdgeAction Action
    {
        get
        {
            return m_edgeAction;
        }
    }

    public Edge()
    {

    }

    public Edge(GraphNode one, GraphNode two, EdgeAction action, float cost, Vector3 position)
    {
        m_position = position;
        m_NodeOne = one;
        m_NodeTwo = two;
        m_edgeAction = action;
        m_traversalCost = cost;
    }

}
