import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


capture = cv.VideoCapture("example.avi")
cv.namedWindow("video", cv.WINDOW_AUTOSIZE) 

def adjust_gamma(image, gamma=1.0):
    invgamma = 1/gamma
    brighter_image = np.array(np.power((image/255), invgamma)*255, dtype=np.uint8)
    return brighter_image

while True:
    ret, frame = capture.read()
    if ret:
        frame = cv.resize(frame, dsize=None, fx=0.5, fy=0.5)
        frame = adjust_gamma(frame, gamma=1.5)
        cv.imshow('video', frame)
        pass
    elif frame.empty():
        break
    if cv.waitKey(10) == 27:
        break
