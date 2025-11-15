import cv2
import math
import numpy as np
img = np.zeros((512,512, 3), np.uint8)
centre_x = 256
centre_y = 256
radius = int(math.hypot(centre_x, centre_y))
theta = 0

img[:] = (211,211,211)
while theta<= 360:
    x_end = int(centre_x + radius*math.cos(math.radians(theta)))
    y_end = int(centre_y + radius*math.sin(math.radians(theta)))
    cv2.line(img, (centre_x,centre_y), (x_end, y_end), (0,0,255), 2)
    theta += 15
    
cv2.imshow("Sample" , img)
cv2.waitKey(0)
