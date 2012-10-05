using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class Astar
{
    List<Node> m_OpenNodes;
    List<Node> m_ClosedNodes;

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
        foreach(Node adjacent in start.m_AdjacentNodes)
        {
            m_OpenNodes.Add(adjacent);
        }
        
        //
    }


}
