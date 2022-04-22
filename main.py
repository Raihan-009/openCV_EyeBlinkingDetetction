import cv2
import faceMeshTracker as mt
import eyeBlinkCounter as eb
import measurementMeter as mm


mesh_tracker = mt.MeshDetection()
blink_tracker = eb.BlinkCounter()

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    cv2.rectangle(frame, (10,10), (345,45), (255,255,255), cv2.FILLED)
    cv2.putText(frame, 'Eye Blink Counter', (15,35), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2)
    if ret:
        faces, img = mesh_tracker.findFaceMesh(frame, draw=False)
        if faces:
            face = faces[0]
            value = blink_tracker.blinkCounter(img,face, drawE=True)
            print(value)
            cv2.rectangle(frame, (10,50), (150,95), (255,255,255), cv2.FILLED)
            cv2.putText(frame, "Count : "+ str(value), (15,80), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,74,186), 2)
            cv2.imshow("Framing", img)
    else:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()