using UnityEngine;
using System.Collections;

public class Pather : MonoBehaviour
{
    static Astar m_astar;
    public GameObject m_nodeStartPrefab, m_nodeEndPrefab;
    GameObject m_startNodeMarker, m_endNodeMarker;


    public static Node m_start, m_end;

    // Use this for initialization
    void Awake()
    {
        m_astar = new Astar();

        m_startNodeMarker = (GameObject)Instantiate(m_nodeStartPrefab, new Vector3(0, 1000, 0), Quaternion.identity);
        m_endNodeMarker = (GameObject)Instantiate(m_nodeEndPrefab, new Vector3(0, 1000, 0), Quaternion.identity);
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
            m_astar.ComputePath(m_start, m_end);
    }
}
