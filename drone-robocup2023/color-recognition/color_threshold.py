# this is a simple script that shows how you can get parts of image/video of a specifically wanted color.

import numpy as np
from cv2 import cv2

red_lower1 = np.array([0, 50, 50])
red_upper1 = np.array([10, 255, 255])
red_lower2 = np.array([170, 50, 50])
red_upper2 = np.array([180, 255, 255]) #set lower and upper boundaries for HSV-red

cap = cv2.VideoCapture(0)

while True:

    f, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(hsv, red_lower1, red_upper1)
    mask2 = cv2.inRange(hsv, red_lower2, red_upper2)
    final_mask = mask1 | mask2 # create a mask for red color

    final_mask = cv2.erode(final_mask, None, iterations=3)
    final_mask = cv2.dilate(final_mask, None, iterations=3) #smoothen mask up

    detected_output = cv2.bitwise_and(img, img, mask=final_mask) #set all unwanted colors to black

    cv2.imshow("original", img)
    cv2.imshow("result", detected_output)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
