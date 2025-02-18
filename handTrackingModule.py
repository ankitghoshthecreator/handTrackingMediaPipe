import cv2     #opencv module
import mediapipe as mp     #google media pipe for hand tracking
import time   #check the frame rate
print("hand tracking")


class handDetectro():
    def __init__(self, mode=False, maxHands=2, detectionConf=.5, trackingConf=0.5):
        self.mode= mode
        self.maxHands=maxHands
        self.detectionConf=detectionConf
        self.trackingConf=trackingConf

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionConf,self.trackingConf)
        self. mpDraw = mp.solutions.drawing_utils



    def findHands(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = self.hands.process(imgRGB)

        # print(result.multi_hand_landmarks)

        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                for id, lms in enumerate(handLms.landmark):
                    print(id, lms)
                    h, w, c = img.shape
                    cx, cy = int(lms.x * w), int(lms.y * h)
                # if id==4:
                #   cv2.circle(img, (cx, cy), 15, (255,0,255), cv2.FILLED)

                self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)



def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()  # this will produce the frames
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (80, 100), cv2.FONT_HERSHEY_DUPLEX, 4, (255, 255, 255))

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
