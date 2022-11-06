import cv2 as cv
import numpy as np

def nothing(x):
    pass

cap = cv.VideoCapture(0)
img = cv.imread("galaxybg.jpg")
img = cv.resize(img, [320,240])
# cv.namedWindow("trackbar")
# cv.createTrackbar("huemin", "trackbar", 0, 255, nothing)
# cv.createTrackbar("huemax", "trackbar", 255, 255, nothing)
# cv.createTrackbar("satmin", "trackbar", 0, 255, nothing)
# cv.createTrackbar("satmax", "trackbar", 255, 255, nothing)
# cv.createTrackbar("valmin", "trackbar", 0, 255, nothing)
# cv.createTrackbar("valmax", "trackbar", 255, 255, nothing)


while True:
    _, frame = cap.read()
    frame = cv.resize(frame, [320,240])
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # hmin = cv.getTrackbarPos("huemin", "trackbar")
    # hmax = cv.getTrackbarPos("huemax", "trackbar")
    # smin = cv.getTrackbarPos("satmin", "trackbar")
    # smax = cv.getTrackbarPos("satmax", "trackbar")
    # vmin = cv.getTrackbarPos("valmin", "trackbar")
    # vmax = cv.getTrackbarPos("valmax", "trackbar")

    lower = np.array([33, 42, 0])
    upper = np.array([83, 255, 255])

    mask = cv.inRange(hsv, lower, upper)
    mask = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)
    maskinv = cv.bitwise_not(mask)

    fg = cv.bitwise_and(frame, maskinv)
    newbg = cv.bitwise_and(mask, img)
    result = cv.bitwise_or(newbg, fg)

    # cv.imshow("foreground", fg)
    cv.imshow("result with new background", result)
    cv.imshow("background", img)
    cv.imshow("newbg", newbg)
    cv.imshow("webcam", frame)
    

    cv.waitKey(1)