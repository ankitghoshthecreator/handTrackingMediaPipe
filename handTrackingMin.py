import cv2     #opencv module
import mediapipe as mp     #google media pipe for hand tracking
import time   #check the frame rate
print("hand tracking")


cap= cv2.VideoCapture(0)


mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils


pTime=0
cTime=0

while True:
    success, img= cap.read()  #this will produce the frames

    imgRGB =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result= hands.process(imgRGB)

    #print(result.multi_hand_landmarks)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            for id, lms in enumerate(handLms.landmark):
                print(id, lms)
                h, w, c= img.shape
                cx, cy= int(lms.x*w), int(lms.y*h)
                if id==4:
                   cv2.circle(img, (cx, cy), 15, (255,0,255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    cv2.putText(img, str(int(fps)), (80, 100), cv2.FONT_HERSHEY_DUPLEX, 4, (255, 255,255))









    cv2.imshow("Image", img)
    cv2.waitKey(1)

