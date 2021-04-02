import cv2


img  = cv2.imread('SA.JPG', 1)

gs = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


cv2.imshow('Image', gs)

cv2.imwrite('black.jpg',gs)




