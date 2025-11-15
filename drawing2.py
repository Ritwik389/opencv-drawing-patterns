import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
img[:] = (200,200,200)
radius = 5.5
while radius <= 600:
    cv2.circle(img, (256,256), int(radius), (0,0,255), 2)
    radius *= 1.5
cv2.imshow("Drawing", img)
cv2.waitKey(0)