using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class Graph
{
    List<Node> m_Nodes;
    List<Edge> m_Edges;

    public Graph()
    {
        m_Nodes = new List<Node>();
        foreach (GameObject node in GameObject.FindGameObjectsWithTag("Node"))
        {
            m_Nodes.Add(node.GetComponent<Node>());
        }
    }

    public void Scan()
    {
        foreach (Node node in m_Nodes)
        {
            node.Initialise();
        }
    }
}
