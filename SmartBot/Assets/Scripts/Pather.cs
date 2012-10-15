using UnityEngine;
using System.Collections;

public class Pather : MonoBehaviour
{
    Astar m_astar;
    public Camera m_cam;
    public GameObject m_nodeStartPrefab, m_nodeEndPrefab;
    GameObject m_startNodeMarker, m_endNodeMarker;

    Ray m_ray;
    RaycastHit m_hit;

    public Node m_start, m_end;

    // Use this for initialization
    void Awake()
    {
        m_astar = new Astar();
        m_ray = new Ray();
        m_hit = new RaycastHit();

        m_startNodeMarker = (GameObject)Instantiate(m_nodeStartPrefab, new Vector3(0, 1000, 0), Quaternion.identity);
        m_endNodeMarker = (GameObject)Instantiate(m_nodeEndPrefab, new Vector3(0, 1000, 0), Quaternion.identity);
    }

    // Update is called once per frame
    void Update()
    {
        m_ray = m_cam.ScreenPointToRay(Input.mousePosition);
        if (Physics.Raycast(m_ray, out m_hit, 10000, (1 << 9)))
        {
            if (Input.GetMouseButtonDown(0))
                m_start = m_hit.transform.GetComponent<Node>();
            if (Input.GetMouseButtonDown(1))
                m_end = m_hit.transform.GetComponent<Node>();
        }
        if (Input.GetKeyDown(KeyCode.Return))
            if (m_start != null && m_end != null)
                m_astar.ComputePath(m_start, m_end);

        if (m_start != null)
            if (m_startNodeMarker.transform.position != m_start.m_position)
                m_startNodeMarker.transform.position = m_start.m_position;
        if (m_end != null)
            if (m_endNodeMarker.transform.position != m_end.m_position)
                m_endNodeMarker.transform.position = m_end.m_position;

    }
}
