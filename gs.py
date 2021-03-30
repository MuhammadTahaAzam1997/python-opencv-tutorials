import cv2

img = cv2.imread('SA.jpg',1)
gi = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('First Image',gi)

cv2.waitKey(delay=0)

cv2.destroyWindow('First Image')
