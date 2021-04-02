import cv2

img = cv2.imread('SA.jpg',1)

gs = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('First image', img)

cv2.imshow('Second image',gs)

cv2.waitKey(delay= 5000)

cv2.destroyWindow('First image')
cv2.destroyWindow('Second image')
