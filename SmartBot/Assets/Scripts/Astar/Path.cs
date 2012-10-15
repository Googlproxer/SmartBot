using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class Path
{
    List<Node> m_Nodes;
    List<Edge> m_Edges;

    List<GameObject> m_markers;

    public Path()
    {
        m_Nodes = new List<Node>();
        m_markers = new List<GameObject>();
    }

    public void AddNode(Node nodeToAdd)
    {
            m_Nodes.Insert(0, nodeToAdd);
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
        m_markers.Clear();

    }
}
