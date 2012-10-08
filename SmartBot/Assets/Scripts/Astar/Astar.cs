using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class Astar
{
    List<Node> m_OpenNodes;
    List<Node> m_ClosedNodes;

    Node m_current;

    Path m_ComputedPath;

    Astar()
    {
        m_OpenNodes = new List<Node>();
        m_ClosedNodes = new List<Node>();

        m_ComputedPath = new Path();
    }


    public void ComputePath(Node start, Node end)
    {
        //empty old lists
        m_OpenNodes.Clear();
        m_ClosedNodes.Clear();
        //add inital node
        m_OpenNodes.Add(start);
        start.m_open = true;
        while (m_OpenNodes.Count != 0 || (m_current.m_closed && m_current != end))
        {
            m_current = m_OpenNodes[0];
            m_OpenNodes.RemoveAt(0);
            m_current.m_open = false;
            m_ClosedNodes.Add(m_current);
            m_current.m_closed = true;
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
                    m_OpenNodes.Sort(
                        delegate(Node node1, Node node2)
                        {
                            return node1.m_FCost.CompareTo(node2.m_FCost);
                        }
                            );
                }
                if (adjacent.m_open && adjacent.m_GCost < m_current.m_GCost)
                {
                    adjacent.m_Parent = m_current;
                    adjacent.CalculateLocalFGH(end);
                    //resort list
                    m_OpenNodes.Sort(
                        delegate(Node node1, Node node2)
                        {
                            return node1.m_FCost.CompareTo(node2.m_FCost);
                        }
                            );
                }
            }
            //sort open by f (lowest first)
            m_OpenNodes.Sort(
                delegate(Node node1, Node node2)
                {
                    return node1.m_FCost.CompareTo(node2.m_FCost);
                }
                    );
        }
        //~while
        m_current = end;
        do
        {
            if (m_current == start)
            {
                break;
            }
            m_ComputedPath.AddNode(m_current);
            m_current = m_current.m_Parent;
        } while (true);
        //~do while
    }


}
