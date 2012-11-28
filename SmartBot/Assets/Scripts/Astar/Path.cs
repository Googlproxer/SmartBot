using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class Path
{
    List<Node> m_Nodes;
    List<Edge> m_Edges;
    List<GraphNode> m_GraphNodes;

    List<GameObject> m_markers;

    public List<Node> Nodes
    {
        get
        {
            return m_Nodes;
        }
    }
    public List<Edge> Edges
    {
        get
        {
            return m_Edges;
        }
    }
    public List<GraphNode> GraphNodes
    {
        get
        {
            return m_GraphNodes;
        }
    }

    public Path()
    {
        m_Nodes = new List<Node>();
        m_Edges = new List<Edge>();
        m_GraphNodes = new List<GraphNode>();
        m_markers = new List<GameObject>();
    }

    public void AddNode(Node nodeToAdd)
    {
        m_Nodes.Insert(0, nodeToAdd);
    }

    public void AddNode(GraphNode nodeToAdd)
    {
        m_GraphNodes.Insert(0, nodeToAdd);
    }

    public void AddEdge(Edge edgeToAdd)
    {
        m_Edges.Insert(0, edgeToAdd);
    }

    public void DisplayPath()
    {
        foreach (Node node in m_Nodes)
        {
            m_markers.Add((GameObject)MonoBehaviour.Instantiate(Resources.Load("Prefabs/PathMarker", typeof(GameObject)), node.m_position, Quaternion.identity));
        }
    }

    public void ClearPath()
    {
        foreach (GameObject marker in m_markers)
        {
            GameObject.Destroy(marker);
        }
        m_Nodes.Clear();
        m_Edges.Clear();
        m_markers.Clear();

    }

    public static Path Concatenate(Path[] pathsToConcatenate)
    {
        Path returnPath = new Path();
        for (int i = 0; i < pathsToConcatenate.Length; i++)
        {
            returnPath.m_Nodes.AddRange(pathsToConcatenate[i].Nodes);
            returnPath.m_Edges.AddRange(pathsToConcatenate[i].Edges);
        }
        return returnPath;
    }
}
