using UnityEngine;
using System.Collections;

public class CameraController : MonoBehaviour
{
    public enum CameraState
    {
        overhead,
        follow,
        free,
        none
    }
    public CameraState m_cameraState;				// Set the camera type

    public Transform m_target;

    private GameObject m_gameCam;					// the child camera
    public Vector3 m_camOffset; 					// how far from container the cam should start	
    public float m_zoomSpeed = 10, 					// Speed of zoom
                 m_keySpeed = 200, 					// Speed of pan using keyboard keys
                 m_dragSpeed = 140, 				// Speed of pan using middle mouse to drag
                 m_maxHeight = 20, 					// Zoom out height to transition to when using Map view.
                 m_minHeight = 5, 					// Zoom in height to transition to when using Map view.
                 m_minScrollHeight = 20, 			// Minimum zoom height using scroll wheel. 	
                 m_maxScrollHeight = 200, 			// Maximum zoom height using scroll wheel. 
                 m_boundaryXLow = -100, 			// Low X boundary for camera movement. 
                 m_boundaryXHi = 100, 				// High X boundary for camera movement. 
                 m_boundaryZLow = -100, 			// Low Z boundary for camera movement. 
                 m_boundaryZHi = 100, 				// Hight Z boundary for camera movement. 
                 m_lowAngle = 40, 					// Camera angle at zoomed in position
                 m_highAngle = 80;					// Camera angle at zoomed out position		 

    public float m_scrollBox = 30;					// How large is the hit area on edge of screen. 
    public float m_scrollSpeed = 50;				// Speed at which the camera translates. 

    private int m_currentAngle = 0; 				// What is the current camera angle.
    public bool m_canZoom = false; 					// Can the player toggle zoom states? // TEMPORARY FOR TESTING \\ 

    void Start()
    {
        m_gameCam = gameObject.GetComponentInChildren<Camera>().gameObject;
        m_gameCam.transform.localPosition = m_camOffset;
        m_gameCam.transform.LookAt(gameObject.transform);	// watch camera container
    }

    void Update()
    {
        // Camera functionality
        switch (m_cameraState)
        {
            case CameraState.overhead:
                PlayerControl();
                break;
            case CameraState.free:

                break;
            case CameraState.follow:
                FollowTarget();
                break;
            case CameraState.none:
                //Do nothing
                break;
            default:
                Debug.Log("CameraState: No state found");
                break;
        }
    }

    void FollowTarget()
    {

            transform.position = m_target.position + new Vector3(-30, 100, 0);
    }

    void PlayerControl()
    {
        // Clear camera translation.
        var camTranslation = Vector3.zero;
        float camZoom = 0;

        // Altering vector direction depending on camera rotation
        Vector3 tempForward = gameObject.transform.TransformDirection(Vector3.forward);
        Vector3 tempLeft = gameObject.transform.TransformDirection(Vector3.left);
        Vector3 tempRight = gameObject.transform.TransformDirection(Vector3.right);

        // Zoom in and out with mousewheel.
        camZoom -= Vector3.up.y * m_zoomSpeed * Input.GetAxis("Mouse ScrollWheel") * Time.deltaTime;

        // Use arrow/WASD keys to move camera.
        if (Input.GetKey(KeyCode.UpArrow) || Input.GetKey(KeyCode.W))
            camTranslation += tempForward * m_keySpeed * Time.deltaTime;
        if (Input.GetKey(KeyCode.DownArrow) || Input.GetKey(KeyCode.S))
            camTranslation += tempForward * -m_keySpeed * Time.deltaTime;
        if (Input.GetKey(KeyCode.LeftArrow) || Input.GetKey(KeyCode.A))
            camTranslation += tempLeft * m_keySpeed * Time.deltaTime;
        if (Input.GetKey(KeyCode.RightArrow) || Input.GetKey(KeyCode.D))
            camTranslation += tempRight * m_keySpeed * Time.deltaTime;

        // Drag camera around using Middle-mouse button.
        if (Input.GetMouseButton(2))
        {
            switch (m_currentAngle)
            {
                case 0:
                    camTranslation -= new Vector3(Input.GetAxis("Mouse X") * m_dragSpeed * Time.deltaTime, 0,
                                       Input.GetAxis("Mouse Y") * m_dragSpeed * Time.deltaTime);
                    break;
                case 1:
                    camTranslation -= new Vector3(Input.GetAxis("Mouse Y") * m_dragSpeed * Time.deltaTime, 0,
                                       -Input.GetAxis("Mouse X") * m_dragSpeed * Time.deltaTime);
                    break;
                case 2:
                    camTranslation -= new Vector3(-Input.GetAxis("Mouse X") * m_dragSpeed * Time.deltaTime, 0,
                                       -Input.GetAxis("Mouse Y") * m_dragSpeed * Time.deltaTime);
                    break;
                case 3:
                    camTranslation -= new Vector3(-Input.GetAxis("Mouse Y") * m_dragSpeed * Time.deltaTime, 0,
                                       Input.GetAxis("Mouse X") * m_dragSpeed * Time.deltaTime);
                    break;
            }
        }

        // Define zoom max/min	
        var nextPosition = m_gameCam.transform.position + camTranslation;
        var nextZoomPosition = m_gameCam.transform.position.y + camZoom;

        // Map zoom
        if (nextPosition.y < m_minHeight || m_maxHeight < nextPosition.y)
        {
            camTranslation.y = 0;
        }

        // Scroll zoom
        if (nextZoomPosition < m_minScrollHeight || m_maxScrollHeight < nextZoomPosition)
        {
            camZoom = 0;
        }

        // Perform the move if the next location is within the boundaries/constraints
        if (nextPosition.x > m_boundaryXLow && nextPosition.x < m_boundaryXHi && nextPosition.z < m_boundaryZHi && nextPosition.z > m_boundaryZLow)
        {
            m_gameCam.transform.localPosition += new Vector3(0, camZoom, 0);			// Move the camera, for scroll zoom.
            transform.position += camTranslation;								// move the camera holder.	
        }
    }
}
