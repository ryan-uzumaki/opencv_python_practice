import cv2 as cv
# import matplotlib.pyplot as plt
import numpy as np


capture = cv.VideoCapture("example.avi")
cv.namedWindow("video", cv.WINDOW_AUTOSIZE) 

while True:
    ret, frame = capture.read()
    if ret:
        frame = cv.resize(frame, dsize=None, fx=0.5, fy=0.5)
        cv.imshow('video', frame)
        pass
    else:
        break
    if cv.waitKey(10) == 27:
        break
