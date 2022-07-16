import cv2 as cv

capture = cv.VideoCapture(1)
capture.set(cv.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
cv.namedWindow("frame", cv.WINDOW_AUTOSIZE)

while True:
    ret, frame = capture.read()
    if ret:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faceCascade = cv.CascadeClassifier('face_detect.xml')
        faceRect = faceCascade.detectMultiScale(gray, 1.1, 6)
        for (x, y, w, h) in faceRect:
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.imshow('frame', frame)
    else:
        break
    # if cv.waitKey(10) == ord('q'):
    if cv.waitKey(10) == 27:
        break
