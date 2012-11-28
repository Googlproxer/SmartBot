using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class Graph
{
    List<Node> m_Nodes;
    List<Edge> m_Edges;
    List<GraphNode> m_GraphNodes;

    public List<GraphNode> GraphNodes
    {
        get
        {
            return m_GraphNodes;
        }
    }

    public Graph()
    {
        m_Nodes = new List<Node>();
        foreach (GameObject node in GameObject.FindGameObjectsWithTag("Node"))
        {
            m_Nodes.Add(node.GetComponent<Node>());
        }
    }

    public void ClearGraph()
    {
        if (m_Nodes != null)
            m_Nodes.Clear();
        if (m_Edges != null)
            m_Edges.Clear();
        if (m_GraphNodes != null)
            m_GraphNodes.Clear();
    }

    public Graph(Collider[] nodes)
    {
        m_GraphNodes = new List<GraphNode>();
        m_Edges = new List<Edge>();
        for (int i = 0; i < nodes.Length; i++)
        {
            switch (nodes[i].gameObject.tag)
            {
                case "Door":
                    m_GraphNodes.Add(new GraphNode(nodes[i].gameObject.transform.position, GraphNode.NodeType.NT_Door));
                    break;
                case "Cover":
                    m_GraphNodes.Add(new GraphNode(nodes[i].gameObject.transform.position, GraphNode.NodeType.NT_Cover));
                    break;
                case "Target":
                    m_GraphNodes.Add(new GraphNode(nodes[i].gameObject.transform.position, GraphNode.NodeType.NT_Target));
                    break;
            }
        }
        BuildGraph();

    }

    void BuildGraph()
    {
        //line of sight to each object?
        bool edgeExists = false;
        m_Edges.Clear();
        for (int i = 0; i < m_GraphNodes.Count; i++)
        {
            for (int j = 0; j < m_GraphNodes.Count; j++)
            {
                if (m_GraphNodes[j] != m_GraphNodes[i])
                {
                    edgeExists = false;
                    foreach (Edge edge in m_Edges)
                    {
                        if ((edge.m_NodeOne == m_GraphNodes[j] && edge.m_NodeTwo == m_GraphNodes[i]) || (edge.m_NodeOne == m_GraphNodes[i] && edge.m_NodeTwo == m_GraphNodes[j]))
                        {
                            edgeExists = true;
                            break;
                        }
                    }
                    if (!edgeExists)
                    {
                        if (m_GraphNodes[j].Type != GraphNode.NodeType.NT_Target && m_GraphNodes[i].Type != GraphNode.NodeType.NT_Target)
                        {
                            m_Edges.Add(new Edge(m_GraphNodes[i], m_GraphNodes[j], Edge.EdgeAction.EA_Move, (m_GraphNodes[j].m_position - m_GraphNodes[i].m_position).magnitude, (m_GraphNodes[j].m_position - m_GraphNodes[i].m_position) / 2));
                            if (!m_GraphNodes[i].m_AdjacentNodes.Contains(m_GraphNodes[j]))
                                m_GraphNodes[i].m_AdjacentNodes.Add(m_GraphNodes[j]);
                            if (!m_GraphNodes[j].m_AdjacentNodes.Contains(m_GraphNodes[i]))
                                m_GraphNodes[j].m_AdjacentNodes.Add(m_GraphNodes[i]);
                            if (!m_GraphNodes[i].m_ConnectedEdges.Contains(m_Edges[m_Edges.Count - 1]))
                                m_GraphNodes[i].m_ConnectedEdges.Add(m_Edges[m_Edges.Count - 1]);
                            if (!m_GraphNodes[j].m_ConnectedEdges.Contains(m_Edges[m_Edges.Count - 1]))
                                m_GraphNodes[j].m_ConnectedEdges.Add(m_Edges[m_Edges.Count - 1]);
                            Debug.DrawLine(m_GraphNodes[i].m_position, m_GraphNodes[j].m_position, Color.blue, 100f);
                        }
                        else
                        {
                            if (m_GraphNodes[i].Type == GraphNode.NodeType.NT_Cover || m_GraphNodes[j].Type == GraphNode.NodeType.NT_Cover)
                            {
                                m_Edges.Add(new Edge(m_GraphNodes[i], m_GraphNodes[j], Edge.EdgeAction.EA_Shoot, (m_GraphNodes[j].m_position - m_GraphNodes[i].m_position).magnitude * 2, (m_GraphNodes[j].m_position - m_GraphNodes[i].m_position) / 2));
                                if (!m_GraphNodes[i].m_AdjacentNodes.Contains(m_GraphNodes[j]))
                                    m_GraphNodes[i].m_AdjacentNodes.Add(m_GraphNodes[j]);
                                if (!m_GraphNodes[j].m_AdjacentNodes.Contains(m_GraphNodes[i]))
                                    m_GraphNodes[j].m_AdjacentNodes.Add(m_GraphNodes[i]);
                                if (!m_GraphNodes[i].m_ConnectedEdges.Contains(m_Edges[m_Edges.Count - 1]))
                                    m_GraphNodes[i].m_ConnectedEdges.Add(m_Edges[m_Edges.Count - 1]);
                                if (!m_GraphNodes[j].m_ConnectedEdges.Contains(m_Edges[m_Edges.Count - 1]))
                                    m_GraphNodes[j].m_ConnectedEdges.Add(m_Edges[m_Edges.Count - 1]);
                                Debug.DrawLine(m_GraphNodes[i].m_position, m_GraphNodes[j].m_position, Color.yellow, 100f);
                            }
                        }
                    }
                }
            }
        }
    }


    public void Scan()
    {
        if (m_Edges == null || m_Edges.Count == 0)
        {
            foreach (Node node in m_Nodes)
            {
                node.Initialise();
            }
        }
        else
        {
            Debug.LogWarning("Wrong Graph, this graph is not a navigational graph");
        }
    }
}
