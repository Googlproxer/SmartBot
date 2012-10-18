using UnityEngine;
using System.Collections;
using UnityEditor;

public class FloodFillNodes : EditorWindow
{
    int width, height, depth, offset;
	GameObject NodePrefab, parent;

	// Add menu named "My Window" to the Window menu
	[MenuItem("Utilities/Flood Fill")]
	static void Init()
	{
		// Get existing open window or if none, make a new one:
		FloodFillNodes window = (FloodFillNodes)EditorWindow.GetWindow(typeof(FloodFillNodes));
		if (window)
		{
			//Gets rid of window unused variable warning	
		}

	}

	void OnGUI()
	{
		GUILayout.Label("Settings", EditorStyles.boldLabel);

		EditorGUILayout.BeginVertical();
        width = EditorGUILayout.IntField("Width : ", width);
        height = EditorGUILayout.IntField("Height : ", height);
        depth = EditorGUILayout.IntField("Depth : ", depth);
        offset = EditorGUILayout.IntField("Offset : ", offset);
        NodePrefab = (GameObject)EditorGUILayout.ObjectField("Node Prefab : ", NodePrefab, typeof(GameObject), true);
        parent = (GameObject)EditorGUILayout.ObjectField("Parent Object : ", parent, typeof(GameObject), true);

		if (GUILayout.Button("Apply"))
        {
            NodePrefab.GetComponent<Node>().m_offset = offset;
            SpawnNodes();
		}

		EditorGUILayout.EndHorizontal();
	}

    void SpawnNodes()
    {
        for (int i = 0; i < width; i++)
        {
            for (int j = 0; j < height; j++)
            {
                for (int k = 0; k < depth; k++)
                {
                    GameObject spawned = (GameObject)Instantiate(NodePrefab, new Vector3(i * offset, k * offset, j * offset), Quaternion.identity);
                    spawned.transform.parent = parent.transform;
                }
            }
        }
    }
}
