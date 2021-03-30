import cv2

img = cv2.imread('SA.jpg',1)

cv2.imshow('Window',img)

cv2.waitKey(delay=0)

cv2.destroyWindow('window')
