import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('messi.jpg',1)

imgc =img.copy()


#img,pt1,pt2,color,thickness
cv2.line(imgc,(100,300),(300,50),(255,255,0),5)

cv2.imshow('abc',imgc[...,::-1])
