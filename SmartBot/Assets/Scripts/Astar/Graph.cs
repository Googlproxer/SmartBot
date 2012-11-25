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

    public Graph(GameObject[] nodes)
    {
        m_Nodes = new List<Node>();
        m_Edges = new List<Edge>();
        for(int i = 0; i < nodes.Length; i++)
        {
            switch(nodes[i].tag)
            {
                case "Door":
                    m_Nodes.Add(new Node(nodes[i].transform.position, Node.NodeType.NT_Door));
                    break;
                case "Cover":
                    m_Nodes.Add(new Node(nodes[i].transform.position, Node.NodeType.NT_Cover));
                    break;
                case "Target":
                    m_Nodes.Add(new Node(nodes[i].transform.position, Node.NodeType.NT_Target));
                    break;
            }
        }


    }

    void BuildGraph()
    {
        //line of sight to each object?
        //
    }


    public void Scan()
    {
        foreach (Node node in m_Nodes)
        {
            node.Initialise();
        }
    }
}
