using UnityEngine;
using System.Collections;

public class Edge : MonoBehaviour
{
    Node m_NodeOne, m_NodeTwo;
    //TODO: implement this
    public bool m_oneIsParent;

    public enum EdgeAction
    {
        EA_Shoot,
        EA_Move
    }
    EdgeAction m_edgeAction;

    public Edge(Node one, Node two, EdgeAction action)
    {
        m_NodeOne = one;
        m_NodeTwo = two;
        m_edgeAction = action;

    }

}
