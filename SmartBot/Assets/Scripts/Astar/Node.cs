using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class Node : MonoBehaviour
{
    public Vector3 m_position;
    public List<Node> m_AdjacentNodes;      /* TODO: replace with accessors */
    public List<Edge> m_ConnectedEdges;

    public bool m_useOverlapSphereForAdjacents = true;
    public float m_offset = 32;
    public bool m_walkable = true;
    public bool m_open, m_closed;

    public Node m_Parent;

    /* F = G + H*/
    public float m_FCost, m_GCost, m_HCost;                   /* TODO: replace with accessors */

    void Awake()
    {
        m_AdjacentNodes = new List<Node>();
        m_ConnectedEdges = new List<Edge>();

        m_position = transform.position;


        if (m_useOverlapSphereForAdjacents)
        {
            m_AdjacentNodes.Clear();

            Collider[] adjacents = Physics.OverlapSphere(m_position, m_offset * 1.4f, (1 << 9));
            foreach (Collider node in adjacents)
            {
                if (node.gameObject != gameObject)
                {
                    m_AdjacentNodes.Add(node.gameObject.GetComponent<Node>());
                }
            }
        }
        m_FCost = m_GCost = m_HCost = 0;
        m_open = m_closed = false;
    }

    public void CalculateLocalFGH(Node goalNode)
    {
        bool canContinue = true;
        if (m_Parent == null)
        {
            Debug.LogError("Can't calculate FGH's, No Parent");
            canContinue = false;
        }
        if (goalNode == null)
        {
            Debug.LogError("Can't calculate FGH's, No goal");
            canContinue = false;
        }
        if (canContinue)
        {
            //calc g
            m_GCost = Mathf.Abs((m_Parent.m_position - m_position).magnitude);
            //calc h
            m_HCost = Mathf.Abs((goalNode.m_position - m_position).magnitude);
            //calc f
            m_FCost = m_GCost + m_HCost;
        }
    }
}
