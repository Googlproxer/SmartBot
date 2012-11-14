using UnityEngine;
using System.Collections;

public class Pather : MonoBehaviour
{
    static Astar m_astar;
    public GameObject m_nodeStartPrefab, m_nodeEndPrefab;
    GameObject m_startNodeMarker, m_endNodeMarker;


    public static Node m_start, m_end;

    static Path[] m_subPaths;
    static Path m_finalPath;
    public static Path PathVia
    {
        get
        {
            return m_finalPath;
        }
    }

    // Use this for initialization
    void Awake()
    {
        m_astar = new Astar();

        m_startNodeMarker = (GameObject)Instantiate(m_nodeStartPrefab, new Vector3(0, 1000, 0), Quaternion.identity);
        m_endNodeMarker = (GameObject)Instantiate(m_nodeEndPrefab, new Vector3(0, 1000, 0), Quaternion.identity);
        m_subPaths = new Path[25];
        m_finalPath = new Path();
        for (int i = 0; i < m_subPaths.Length; i++)
        {
            m_subPaths[i] = new Path();
        }
    }

    // Update is called once per frame
    void Update()
    {

        if (m_start != null)
            if (m_startNodeMarker.transform.position != m_start.m_position)
                m_startNodeMarker.transform.position = m_start.m_position;
        if (m_end != null)
            if (m_endNodeMarker.transform.position != m_end.m_position)
                m_endNodeMarker.transform.position = m_end.m_position;

    }

    public static void ComputePath()
    {
        if (m_start != null && m_end != null)
        {
            m_finalPath = m_astar.CalculatePath(m_start, m_end);
        }
    }

    public static void ComputePathVia(Node[] nodesToVisit)
    {

        if (m_start != null && m_end != null)
        {
            if (nodesToVisit.Length > 0)
            {
                //start - 0
                m_subPaths[0] = m_astar.CalculatePath(m_start, nodesToVisit[0]);
                for (int i = 1; i < nodesToVisit.Length; i++)
                {
                    //i-1 - i
                    m_subPaths[i] = m_astar.CalculatePath(nodesToVisit[i - 1], nodesToVisit[i]);
                }
                //i - end
                m_subPaths[nodesToVisit.Length - 1] = m_astar.CalculatePath(nodesToVisit[nodesToVisit.Length - 1], m_end);

                //concatenate paths
                m_finalPath = Path.Concatenate(m_subPaths);
            }
            else
            {
                m_finalPath = m_astar.CalculatePath(m_start, m_end);
            }
        }
    }

    //recursive decision based path calculation
    public static void CalculateWeightedPath()
    {
        int pathNumber = 0;
        bool reachedEnd = false;

        while (!reachedEnd)
        {
            m_subPaths[pathNumber] = m_astar.CalculatePath(m_start, m_end);

            foreach (Node node in m_subPaths[pathNumber].Nodes)
            {
                if (node.Flag != Node.FlagType.FT_None)
                {
                    switch (node.Flag)
                    {
                        case Node.FlagType.FT_Door:

                            break;
                        case Node.FlagType.FT_Cover:

                            break;
                        case Node.FlagType.FT_Choice:

                            break;
                        default:

                            break;
                    }
                    break;
                }
            }
        }
    }
}
