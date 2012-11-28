using UnityEngine;
using System.Collections;

public class CombatDummy : MonoBehaviour
{
    public GameObject m_Target;
    public GameObject m_BulletPrefab;

    Transform m_FirePoint;
    public Vector3 m_targetPosition, actorDirection, firepoint;

    GameObject[] m_bullets;
    bool[] m_bulletsFired;
    public int m_clipSize;
    public float m_fireRate;
    float m_fireTimer;

    bool m_reloading;
    bool m_reloaded;

    public float m_reloadTime;
    float m_reloadtimer;

    public float m_health = 100;

    // Use this for initialization
    void Start()
    {
        foreach (Transform child in transform)
        {
            if (child.tag == "FirePoint")
            {
                m_FirePoint = child;
                break;
            }
        }
        m_bullets = new GameObject[m_clipSize];
        for (int i = 0; i < m_clipSize; i++)
        {
            m_bullets[i] = (GameObject)Instantiate(m_BulletPrefab, m_FirePoint.position, Quaternion.identity);
            m_bullets[i].renderer.enabled = false;
        }
        m_bulletsFired = new bool[m_clipSize];
        for (int i = 0; i < m_clipSize; i++)
        {
            m_bulletsFired[i] = false;
        }
        m_reloading = false;
        m_reloaded = true;
        m_reloadtimer = 0;
        m_fireTimer = 0;
        m_targetPosition = new Vector3(m_Target.transform.position.x, 16, m_Target.transform.position.z);
    }

    // Update is called once per frame
    void Update()
    {
        m_targetPosition = new Vector3(m_Target.transform.position.x, 16, m_Target.transform.position.z);
        actorDirection = (m_FirePoint.position - m_targetPosition).normalized;
        firepoint = m_FirePoint.position;
        m_fireTimer += Time.deltaTime;
        if (!m_reloading)
        {
            if (CheckFiringLine(firepoint, m_targetPosition))
            {
                if (m_fireTimer >= m_fireRate)
                {
                    m_fireTimer = 0;
                    Fire();
                }
                transform.LookAt(m_targetPosition);
            }
        }
        UpdateBullets();
        if (m_health <= 0)
        {
            transform.position = Vector3.zero;
        }
    }

    void UpdateBullets()
    {
        if (!m_reloading)
        {
            for (int i = 0; i < m_clipSize; i++)
            {
                if (m_bulletsFired[i])
                {
                    m_bullets[i].transform.position += ((m_FirePoint.position - m_targetPosition).normalized + m_FirePoint.position) * Time.deltaTime;
                }
            }
        }
        else
        {
            if (!m_reloaded)
            {
                for (int i = 0; i < m_clipSize; i++)
                {
                    m_bullets[i].renderer.enabled = false;
                    m_bullets[i].transform.position = m_FirePoint.position;
                    m_bulletsFired[i] = false;
                }
                m_reloaded = true;
            }
            m_reloadtimer += Time.deltaTime;
            if (m_reloadtimer >= m_reloadTime)
            {
                m_reloadtimer = 0;
                m_reloading = false;
            }
        }
    }

    void Fire()
    {
        for (int i = 0; i < m_clipSize; i++)
        {
            if (!m_bulletsFired[i])
            {
                m_bulletsFired[i] = true;
                m_bullets[i].renderer.enabled = true;
                break;
            }
            if (i == m_clipSize - 1 && m_bulletsFired[i])
            {
                Reload();
                break;
            }
        }
    }

    void Reload()
    {
        if (!m_reloading)
        {
            m_reloading = true;
            m_reloaded = false;
        }
    }


    public static bool CheckFiringLine(Vector3 startPos, Vector3 endPos)
    {
        int layerMask = (1 << 8) | (1 << 10);//Layer mask to only collide against walls

        if (Physics.Linecast(startPos, endPos, layerMask))//If we hit a wall
        {
            Debug.DrawLine(startPos, endPos, Color.red, 1f);
            return false;//Return false
        }
        else//If we don't
        {
            Debug.DrawLine(startPos, endPos, Color.green, 1f);
            return true;//Return true
        }
    }
}
