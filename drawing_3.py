import cv2
import numpy as np
import math

img = np.zeros((512,512,3), np.uint8)
img[:] = (110,110,110)
cv2.circle(img, (320,150),10 , (197,168,50), cv2.FILLED)
cv2.circle(img, (192,150),10 , (197,168,50), cv2.FILLED)
thickness = 10
centre = (256,256)
color = (197,168,50)
cv2.line(img, (256,0), (256,512), color, thickness)
cv2.line(img, centre, (0,600), color, thickness)
cv2.line(img, centre, (450,512), color, thickness)
cv2.line(img, (256,0), (512,256), color, thickness) #triangle
cv2.line(img, (256,0), (0,256), color, thickness) #triangle   
cv2.line(img, (0,256), (512,256), color, thickness) #triangle

cv2.imshow("Drawing", img)
cv2.waitKey(0)
