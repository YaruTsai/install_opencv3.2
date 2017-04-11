# coding:utf-8

import cv2
import numpy as np

#img = cv2.imread("big.png")
#cropped = img[11:51, 961:1001]
#cv2.imwrite("mcu_green.png", cropped)

image1 = cv2.imread("mcu_green.png")
image2 = cv2.imread("mcu_red.png")

diff = cv2.subtract(image2, image1)

#if difference is all zeros it will return False.
result = not np.any(diff)

if result is True:
    print "The images are the same."
else:
    cv2.imwrite("result2.png", diff)
    print "The images are differenct."