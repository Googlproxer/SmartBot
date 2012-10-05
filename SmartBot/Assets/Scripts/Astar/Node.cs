using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class Node : MonoBehaviour
{
    public Vector3 m_position;

    public List<Node> m_AdjacentNodes;      /* TODO: replace with accessors */
    public List<Edge> m_ConnectedEdges;

    Node m_Parent;

    /* F = G + H*/
    public float m_FCost;                   /* TODO: replace with accessors */
    public float m_GCost;
    public float m_HCost;

    void Awake()
    {
        m_AdjacentNodes = new List<Node>();
        m_ConnectedEdges = new List<Edge>();

        m_position = transform.position;

        //use an overlapsphere to get the adjacents
    }

    public void CalculateFs()
    {
        foreach (Node adjacent in m_AdjacentNodes)
        {
            adjacent.m_FCost = adjacent.m_GCost + adjacent.m_HCost;
        }
    }

    public void CalculateGs()
    {
        foreach (Node adjacent in m_AdjacentNodes)
        {
            adjacent.m_GCost = Mathf.Abs((adjacent.m_position - m_position).sqrMagnitude);
        }
    }

    public void CalculateHs(Node goalNode)
    {
        foreach (Node adjacent in m_AdjacentNodes)
        {
            adjacent.m_HCost = Mathf.Abs((goalNode.m_position - adjacent.m_position).sqrMagnitude);
        }
    }
}
