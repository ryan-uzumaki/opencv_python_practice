import cv2 as cv
import numpy as np


image = cv.imread("test.png")

img = cv.resize(image, dsize=None, fx=0.2, fy=0.2)
# img = cv.resize(image, (image.shape[1]//2, image.shape[0]//2))
cv.imshow("img", img)
# blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)
B, G, R = cv.split(img)

img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("img_hsv", img_hsv)
print(img_hsv.dtype)
print(img_hsv[2])
# cv.imshow("img_hsv[2]", img_hsv[2])

# cv.imshow("split channelB", B)
# cv.imshow("split channelG", G)
# cv.imshow("split channelR", R)


# bmg = B-G
# cv.imshow("bmgmr", bmg)
# bmg = B - G
# gmb = G - B
# cv.imshow("bmg", bmg)
# cv.imshow("gmb", gmb)
# rmb = R - B
# bmr = B - R
# cv.imshow("rmb", rmb)
# cv.imshow("bmr", bmr)
# rmg = R - G
# gmr = G - R
# cv.imshow("rmg", rmg)
# cv.imshow("gmr", gmr)
# ksize = (5, 5)
# image_blur = cv.blur(bmg, ksize)
# cv.imshow("image_blur", image_blur)
# image_result = cv.threshold(image_blur, 50, 255, cv.THRESH_BINARY)
# # gmr = channel[1]-channel[2]
# # rmg = channel[2]-channel[1]
# # cv.imshow("gmr", gmr)
# # cv.imshow("rmg", rmg)
# cv.imshow("image_result", image_result)
cv.waitKey(0)


# cv.calcHist(img, [0], None, [255], [0,255])