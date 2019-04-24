#Roman Alonzo
#AIA Club Project

import cv2
import numpy as np

def main():
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    capture = cv2.VideoCapture(0)
    while(True):
        ret, frame = capture.read()
        faces = faceCascade.detectMultiScale(frame, scaleFactor= 1.5, minNeighbors=5, minSize=(40,40), flags = cv2.CASCADE_SCALE_IMAGE)
        frame = cv2.resize(frame, 800, 600)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 3)

        cv2.imshow("This is our video", frame)
        cv2.waitKey(1)
main()