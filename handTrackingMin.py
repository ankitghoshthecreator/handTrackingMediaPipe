import cv2     #opencv module
import mediapipe as mp     #google media pipe for hand tracking
import time   #check the frame rate
print("hand tracking")


cap= cv2.VideoCapture(0)

while True:
    success, img= cap.read()  #this will produce the frames

    cv2.imshow("Image", img)
    cv2.waitKey(1)

