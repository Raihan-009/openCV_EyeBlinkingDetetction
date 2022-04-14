import cv2
import faceMeshTracker as mt
import eyeBlinkCounter as eb
import measurementMeter as mm


mesh_tracker = mt.MeshDetection()
blink_tracker = eb.BlinkCounter()

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    if ret:
        faces, img = mesh_tracker.findFaceMesh(frame, draw=False)
        if faces:
            face = faces[0]
            value = blink_tracker.blinkCounter(img,face, drawE=False)
            print(value)
            cv2.imshow("Framing", img)
    else:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()