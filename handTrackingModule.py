import cv2  # OpenCV module
import mediapipe as mp  # Google MediaPipe for hand tracking
import time  # Check the frame rate

print("hand tracking")


class HandDetector:
    def __init__(self, mode=False, maxHands=2, detectionConf=0.5, trackingConf=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionConf = detectionConf
        self.trackingConf = trackingConf

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectionConf,
            min_tracking_confidence=self.trackingConf
        )
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img
    def findPosation(self, img, handNo=0, draw=True):

        lmList=[]
        if self.results.multi_hand_landmarks:
            for id, lms in enumerate(handLms.landmark):
                print(id, lms)
                h, w, c = img.shape
                cx, cy = int(lms.x * w), int(lms.y * h)
                # if id==4:
                cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        return lmList


def main():
    pTime = 0
    cap = cv2.VideoCapture(0)

    detector = HandDetector()

    while True:
        success, img = cap.read()
        if not success:
            break

        img = detector.findHands(img)

        cTime = time.time()
        fps = 1 / (cTime - pTime) if (cTime - pTime) > 0 else 0
        pTime = cTime

        cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 2)

        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
