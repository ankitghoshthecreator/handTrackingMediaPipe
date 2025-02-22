import cv2  # OpenCV module
import mediapipe as mp  # Google MediaPipe for hand tracking
import time  # Check the frame rate
import handTrackingModule as hmt



pTime = 0
cap = cv2.VideoCapture(0)

detector = hmt.HandDetector()

while True:
    success, img = cap.read()
    if not success:
        break

    img = detector.findHands(img)
    lmList=detector.findPosation(img)
    if len(lmList) !=0:
        print(lmList[2])


    cTime = time.time()
    fps = 1 / (cTime - pTime) if (cTime - pTime) > 0 else 0
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break