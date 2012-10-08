using UnityEngine;
using System.Collections;
using UnityEditor;

public class FloodFillNodes : EditorWindow
{
    int width, height;
	GameObject NodePrefab;

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
		NodePrefab = (GameObject)EditorGUILayout.ObjectField("Node Prefab : ", NodePrefab, typeof(GameObject), true);

		if (GUILayout.Button("Apply"))
		{
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
                Instantiate(NodePrefab, new Vector3(i * 32, 1, j * 32), Quaternion.identity);
            }
        }
    }
}
