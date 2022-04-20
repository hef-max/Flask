import cv2.cv2 as cv2
import numpy as np
import time
import os
import HandTrackingModule as htm



folder = r"C:\Users\HEFRY ANESTI\Desktop\programing\Flask\latihan4\Header"
mylist = os.listdir(folder)
print(mylist)

overlaylist = []
for imPath in mylist:
    image = cv2.imread(f'{folder}/{imPath}')
    overlaylist.append(image)

print(len(overlaylist))

#####
brushThickness = 15
eraserThickness = 50
#####

detector = htm.handDetector(detectionCon=0.75)
imageCanvas = np.zeros((460, 680, 3), np.uint8)
drawColor = (255, 0, 255)

class VideoCamera(object):

    def __init__(self):
        self.drawColor = (255, 0, 255)
        self.cap = cv2.VideoCapture(0)
        # cap.set(3, 1280)
        # cap.set(4, 720)

    def get_frame(self):
        self.brushThickness = 15
        self.eraserThickness = 50

        header = overlaylist[0]
        self.header = header

        _, img = self.cap.read()
        img = cv2.resize(img, (680, 460))
        img = cv2.flip(img, 1)

        img = detector.findHands(img=img)
        lmlis = detector.findPosition(img, draw=False)

        if len(lmlis) != 0:
            # print(lmlis)
            x1, y1 = lmlis[8][1:]
            x2, y2 = lmlis[12][1:]
        
            fingers = detector.fingersUp()
            # print(fingers)

            if fingers[1] and fingers[2]:
                self.xp, self.yp = 0, 0
                # cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)
                # print("selection mode")
                if y1 < 125:
                    if 250 < x1 < 450:
                        self.header = overlaylist[0]
                        self.drawColor = (255, 0, 255)
                    # elif 550 < x1 < 750:
                    #     header = overlaylist[0]
                    #     drawColor = (255, 0, 0)
                    # elif 800 < x1 < 950:
                    #     header = overlaylist[1]
                        # drawColor = (0, 255, 0)
                    elif 500 < x1 < 700:
                        self.header = overlaylist[0]
                        self.drawColor = (0, 0, 0)
                        
                    cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), self.drawColor, cv2.FILLED)

            if fingers[1] and fingers[2] == False:
                cv2.circle(img, (x1, y1 ), 15, self.drawColor, cv2.FILLED)
                # print("Drawing mode")

                if self.xp == 0 and self.yp == 0:
                    self.xp, self.yp = x1, y1
                
                if self.drawColor == (0, 0, 0):
                    cv2.line(img, (self.xp, self.yp), (x1, y1), self.drawColor, self.eraserThickness)
                    cv2.line(imageCanvas, (self.xp, self.yp), (x1, y1), self.drawColor, self.eraserThickness)
                
                else:
                    cv2.line(img, (self.xp, self.yp), (x1, y1), self.drawColor, self.brushThickness)
                    cv2.line(imageCanvas, (self.xp, self.yp), (x1, y1), self.drawColor, self.brushThickness)

                self.xp, self.yp = x1, y1
        
        imgGray = cv2.cvtColor(imageCanvas, cv2.COLOR_BGR2GRAY)
        _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
        imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
        img = cv2.bitwise_and(img, imgInv)
        img = cv2.bitwise_or(img, imageCanvas)
        
        # img = cv2.addWeighted(img, 0.5, imageCanvas, 0.5, 0)
        # cv2.imshow("Image", img)
        # cv2.imshow("canvas", imageCanvas)
        # if cv2.waitKey(1) == 27:
            # break
        ret, jpeg = cv2.imencode('.jpg', img)
        return jpeg.tobytes()
