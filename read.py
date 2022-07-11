import cv2 as cv

# img = cv.imread("opencv-course-master/Resources/Photos/cat_large.jpg")
capture = cv.VideoCapture("opencv-course-master/Resources/Videos/dog.mp4")
# cv.namedWindow("Cat", cv.WINDOW_NORMAL)
# cv.imshow("Cat", img)
# cv.imshow("Cat", capture)
# cv.waitKey(0)

while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break
    cv.imshow("Video", frame)
    if cv.waitKey(20) == 27:
        break

capture.release()
cv.destroyAllWindows()

