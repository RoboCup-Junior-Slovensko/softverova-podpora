import cv2
import numpy as np
from djitellopy import tello

def empty(a):
    pass

cv2.namedWindow("TestColorHSV")
cv2.resizeWindow("TestColorHSV", 500,240)
cv2.createTrackbar("HMin","TestColorHSV",0,179,empty)
cv2.createTrackbar("HMax","TestColorHSV",19,179,empty)
cv2.createTrackbar("SMin","TestColorHSV",110,255,empty)
cv2.createTrackbar("SMax","TestColorHSV",240,255,empty)
cv2.createTrackbar("VMin","TestColorHSV",153,255,empty)
cv2.createTrackbar("VMax","TestColorHSV",255,255,empty)


# cap = cv2.VideoCapture(0)
me = tello.Tello()
me.connect()
me.streamon()

while True:
    # img = cv2.imread("resources/path.png")
    # img2 = cv2.imread('resources/colors.png')
    # imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # imgHSV2 = cv2.cvtColor(img2,cv2.COLOR_BGR2HSV)
    # _, img = cap.read()
    img = me.get_frame_read().frame
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("HMin","TestColorHSV")
    h_max = cv2.getTrackbarPos("HMax", "TestColorHSV")
    s_min = cv2.getTrackbarPos("SMin", "TestColorHSV")
    s_max = cv2.getTrackbarPos("SMax", "TestColorHSV")
    v_min = cv2.getTrackbarPos("VMin", "TestColorHSV")
    v_max = cv2.getTrackbarPos("VMax", "TestColorHSV")

    print(h_min,s_min,v_min,h_max,s_max,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])

    mask = cv2.inRange(imgHSV,lower,upper)
    mask = cv2.erode(mask, np.ones((5, 5), np.uint8), iterations=1)
    mask = cv2.dilate(mask, np.ones((5, 5), np.uint8), iterations=1)
    # mask2 = cv2.inRange(imgHSV2,lower,upper)

    imgResult = cv2.bitwise_and(img,img,mask=mask)
    # imgResult2 = cv2.bitwise_and(img2, img2, mask=mask2)


    cv2.imshow("meno",mask)
    # cv2.imshow("r2",imgResult2)

    cv2.waitKey(1)