import cv2

img = cv2.imread('dog.jpg')
img = cv2.resize(img, (480,360))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('gray', gray)
cv2.imshow('original', img)

cv2.waitKey(0)
cv2.destroyAllWindows()