using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class Astar
{
    public static Astar m_instance;

    List<Node> m_OpenNodes;
    List<Node> m_ClosedNodes;

    List<GraphNode> m_OpenGraphNodes;
    List<GraphNode> m_ClosedGraphNodes;

    GraphNode m_currentGraphNode;

    Node m_current;
    bool m_pathSuccessful;
    Path m_ComputedPath;

    public Path ComputedPath
    {
        get
        {
            return m_ComputedPath;
        }
    }

    public int loopnumber = 0;

    System.Diagnostics.Stopwatch timer;

    public Astar()
    {
        m_OpenNodes = new List<Node>();
        m_ClosedNodes = new List<Node>();

        m_OpenGraphNodes = new List<GraphNode>();
        m_ClosedGraphNodes = new List<GraphNode>();

        m_ComputedPath = new Path();

        timer = new System.Diagnostics.Stopwatch();

        if (m_instance == null)
            m_instance = this;
    }

    [System.Obsolete]
    public void ComputePath(Node start, Node end)
    {
        timer.Start();
        foreach (GameObject gobj in GameObject.FindGameObjectsWithTag("PathMarker"))
        {
            GameObject.Destroy(gobj);
        }
        //remove old path
        m_ComputedPath.ClearPath();
        //empty old lists
        foreach (Node node in m_OpenNodes)
            node.m_open = false;
        m_OpenNodes.Clear();
        m_OpenNodes.TrimExcess();
        foreach (Node node in m_ClosedNodes)
            node.m_closed = false;
        m_ClosedNodes.Clear();
        m_ClosedNodes.TrimExcess();
        //add inital node
        m_OpenNodes.Add(start);
        start.m_open = true;
        while (m_OpenNodes.Count != 0 || (m_current.m_closed && m_current != end))
        {
            loopnumber++;
            if (m_OpenNodes.Count == 0)
            {
                m_pathSuccessful = false;
                break;
            }
            m_current = m_OpenNodes[0];
            m_OpenNodes.RemoveAt(0);
            m_current.m_open = false;
            m_ClosedNodes.Add(m_current);
            m_current.m_closed = true;
            if (m_current == end)
            {
                m_pathSuccessful = true;
                break;
            }
            foreach (Node adjacent in m_current.m_AdjacentNodes)
            {
                if (adjacent.m_walkable == false || adjacent.m_closed)
                    continue;
                if (!adjacent.m_open)
                {
                    m_OpenNodes.Add(adjacent);
                    adjacent.m_open = true;
                    adjacent.m_Parent = m_current;
                    adjacent.CalculateLocalFGH(end);
                    //resort list
                    m_OpenNodes.Sort((node1, node2) => node1.m_FCost.CompareTo(node2.m_FCost));
                }
                if (adjacent.m_open && adjacent.m_GCost < m_current.m_GCost)
                {
                    adjacent.m_Parent = m_current;
                    adjacent.CalculateLocalFGH(end);
                    //resort list
                    m_OpenNodes.Sort((node1, node2) => node1.m_FCost.CompareTo(node2.m_FCost));
                }
            }
            //sort open by f (lowest first)
            m_OpenNodes.Sort((node1, node2) => node1.m_FCost.CompareTo(node2.m_FCost));
        }
        //~while
        loopnumber = 0;
        if (m_pathSuccessful)
        {
            //build path
            m_current = end;
            while (m_current != start)
            {
                m_ComputedPath.AddNode(m_current);
                //if no parent assume its the start
                if (m_current.m_Parent != null)
                    m_current = m_current.m_Parent;
                else
                    break;
            }
            if (m_current == start)
                m_ComputedPath.AddNode(m_current);
            //~while
        }
        else
            Debug.LogWarning("No Path!");
        timer.Stop();
        Debug.Log("Time taken to Calculate Path: " + (float.Parse(timer.ElapsedTicks.ToString()) / 10000).ToString() + "ms");
        timer.Reset();
        timer.Start();
        if (m_pathSuccessful)
            m_ComputedPath.DisplayPath();
        timer.Stop();
        Debug.Log("Time taken to Render Path: " + (float.Parse(timer.ElapsedTicks.ToString()) / 10000).ToString() + "ms");
    }

    public Path CalculatePath(Node start, Node end)
    {
        timer.Start();
        foreach (GameObject gobj in GameObject.FindGameObjectsWithTag("PathMarker"))
        {
            GameObject.Destroy(gobj);
        }
        //remove old path
        m_ComputedPath.ClearPath();
        //empty old lists
        foreach (Node node in m_OpenNodes)
            node.m_open = false;
        m_OpenNodes.Clear();
        m_OpenNodes.TrimExcess();
        foreach (Node node in m_ClosedNodes)
            node.m_closed = false;
        m_ClosedNodes.Clear();
        m_ClosedNodes.TrimExcess();
        //add inital node
        m_OpenNodes.Add(start);
        start.m_open = true;
        while (m_OpenNodes.Count != 0 || (m_current.m_closed && m_current != end))
        {
            loopnumber++;
            if (m_OpenNodes.Count == 0)
            {
                m_pathSuccessful = false;
                break;
            }
            m_current = m_OpenNodes[0];
            m_OpenNodes.RemoveAt(0);
            m_current.m_open = false;
            m_ClosedNodes.Add(m_current);
            m_current.m_closed = true;
            if (m_current == end)
            {
                m_pathSuccessful = true;
                break;
            }
            foreach (Node adjacent in m_current.m_AdjacentNodes)
            {
                if (adjacent.m_walkable == false || adjacent.m_closed)
                    continue;
                if (!adjacent.m_open)
                {
                    m_OpenNodes.Add(adjacent);
                    adjacent.m_open = true;
                    adjacent.m_Parent = m_current;
                    adjacent.CalculateLocalFGH(end);
                    //resort list
                    m_OpenNodes.Sort((node1, node2) => node1.m_FCost.CompareTo(node2.m_FCost));
                }
                if (adjacent.m_open && adjacent.m_GCost < m_current.m_GCost)
                {
                    adjacent.m_Parent = m_current;
                    adjacent.CalculateLocalFGH(end);
                    //resort list
                    m_OpenNodes.Sort((node1, node2) => node1.m_FCost.CompareTo(node2.m_FCost));
                }
            }
            //sort open by f (lowest first)
                    m_OpenNodes.Sort((node1, node2) => node1.m_FCost.CompareTo(node2.m_FCost));
        }
        //~while
        loopnumber = 0;
        if (m_pathSuccessful)
        {
            //build path
            m_current = end;
            while (m_current != start)
            {
                m_ComputedPath.AddNode(m_current);
                //if no parent assume its the start
                if (m_current.m_Parent != null)
                    m_current = m_current.m_Parent;
                else
                    break;
            }
            if (m_current == start)
                m_ComputedPath.AddNode(m_current);
            //~while
        }
        else
        {
            Debug.LogWarning("No Path!");
            return null;
        }
        timer.Stop();
        Debug.Log("Time taken to Calculate Path: " + (float.Parse(timer.ElapsedTicks.ToString()) / 10000).ToString() + "ms");
        timer.Reset();
        if (m_pathSuccessful)
            m_ComputedPath.DisplayPath();
        return m_ComputedPath;
    }

    public Path CalculateEdgeBasedPath(GraphNode start, GraphNode end)
    {
        timer.Start();
        Edge currentEdge = new Edge();
        //remove old path
        m_ComputedPath.ClearPath();
        //empty old lists
        foreach (GraphNode node in m_OpenGraphNodes)
            node.m_open = false;
        m_OpenGraphNodes.Clear();
        m_OpenGraphNodes.TrimExcess();
        foreach (GraphNode node in m_ClosedGraphNodes)
            node.m_closed = false;
        m_ClosedGraphNodes.Clear();
        m_ClosedGraphNodes.TrimExcess();
        //add inital node
        m_OpenGraphNodes.Add(start);
        start.m_open = true;
        while (m_OpenGraphNodes.Count != 0 || (m_currentGraphNode.m_closed && m_currentGraphNode != end))
        {
            if (m_OpenGraphNodes.Count == 0)
            {
                m_pathSuccessful = false;
                break;
            }
            m_currentGraphNode = m_OpenGraphNodes[0];
            m_OpenGraphNodes.RemoveAt(0);
            m_currentGraphNode.m_open = false;
            m_ClosedGraphNodes.Add(m_currentGraphNode);
            m_currentGraphNode.m_closed = true;
            if (m_currentGraphNode == end)
            {
                m_pathSuccessful = true;
                break;
            }
            for (int i = 0; i < m_currentGraphNode.m_AdjacentNodes.Count; i++)// (Node adjacent in m_current.m_AdjacentNodes)
            {
                currentEdge = m_currentGraphNode.m_ConnectedEdges[i];
                if (m_currentGraphNode.m_AdjacentNodes[i].m_walkable == false || m_currentGraphNode.m_AdjacentNodes[i].m_closed)
                    continue;
                if (!m_currentGraphNode.m_AdjacentNodes[i].m_open)
                {
                    m_OpenGraphNodes.Add(m_currentGraphNode.m_AdjacentNodes[i]);
                    m_currentGraphNode.m_AdjacentNodes[i].m_open = true;
                    m_currentGraphNode.m_AdjacentNodes[i].m_Parent = m_currentGraphNode;
                    m_currentGraphNode.m_AdjacentNodes[i].m_ParentEdge = currentEdge;
                    m_currentGraphNode.m_AdjacentNodes[i].CalculateEdgeBasedLocalFGH(end, currentEdge.m_traversalCost);
                    //resort list
                    m_OpenGraphNodes.Sort((node1, node2) => node1.m_FCost.CompareTo(node2.m_FCost));
                }
                if (m_currentGraphNode.m_AdjacentNodes[i].m_open && m_currentGraphNode.m_AdjacentNodes[i].m_GCost < m_currentGraphNode.m_GCost)
                {
                    m_currentGraphNode.m_AdjacentNodes[i].m_Parent = m_currentGraphNode;
                    m_currentGraphNode.m_AdjacentNodes[i].m_ParentEdge = currentEdge;
                    m_currentGraphNode.m_AdjacentNodes[i].CalculateEdgeBasedLocalFGH(end, currentEdge.m_traversalCost);
                    //resort list
                    m_OpenGraphNodes.Sort((node1, node2) => node1.m_FCost.CompareTo(node2.m_FCost));
                }
            }
            //sort open by f (lowest first)
            m_OpenGraphNodes.Sort((node1, node2) => node1.m_FCost.CompareTo(node2.m_FCost));
        }
        //~while
        timer.Stop();

        if (m_pathSuccessful)
        {
            //build path
            m_currentGraphNode = end;
            while (m_currentGraphNode != start)
            {
                m_ComputedPath.AddNode(m_currentGraphNode);
                if (m_currentGraphNode.m_ParentEdge != null)
                {
                    m_ComputedPath.AddEdge(m_currentGraphNode.m_ParentEdge);
                }
                //if no parent assume its the start
                if (m_currentGraphNode.m_Parent != null)
                {
                    m_currentGraphNode = m_currentGraphNode.m_Parent;
                }
                else
                    break;
            }
            if (m_currentGraphNode == start)
                m_ComputedPath.AddNode(m_currentGraphNode);
            //~while
        }
        else
        {
            Debug.LogWarning("No Path!");
            return null;
        }
        Debug.Log("Time taken to Calculate Path: " + (float.Parse(timer.ElapsedTicks.ToString()) / 10000).ToString() + "ms");
        timer.Reset();
        return m_ComputedPath;
    }
}
