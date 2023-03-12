import cv2
import numpy as np

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


while True:
    img = cv2.imread("resources/hsvGraph.png")
    img2 = cv2.imread('resources/colors.png')
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    imgHSV2 = cv2.cvtColor(img2,cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("HMin","TestColorHSV")
    h_max = cv2.getTrackbarPos("HMax", "TestColorHSV")
    s_min = cv2.getTrackbarPos("SMin", "TestColorHSV")
    s_max = cv2.getTrackbarPos("SMax", "TestColorHSV")
    v_min = cv2.getTrackbarPos("VMin", "TestColorHSV")
    v_max = cv2.getTrackbarPos("VMax", "TestColorHSV")

    print(f'| HMIN : {h_min} | HMAX : {h_max} | SMIN : {s_min} | SMAX : {s_max} | VMIN : {v_min} | VMAX : {v_max} |')
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])

    mask = cv2.inRange(imgHSV,lower,upper)
    mask2 = cv2.inRange(imgHSV2,lower,upper)

    imgResult = cv2.bitwise_and(img,img,mask=mask)
    imgResult2 = cv2.bitwise_and(img2, img2, mask=mask2)


    cv2.imshow("hsv_graph",imgResult)
    cv2.imshow("colors",imgResult2)

    cv2.waitKey(1)