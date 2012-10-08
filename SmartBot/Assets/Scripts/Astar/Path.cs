using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class Path
{
    List<Node> m_Nodes;
    List<Edge> m_Edges;

    public Path()
    {
        m_Nodes = new List<Node>();
    }

    Path(Node start, Node end)
    {
        //Astar.ComputePath(start, end);
    }

    public void AddNode(Node nodeToAdd)
    {
        m_Nodes.Insert(0, nodeToAdd);
    }
}
