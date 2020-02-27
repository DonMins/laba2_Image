import  cv2
import cv
from skimage import img_as_float, img_as_ubyte
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("rab.jpg",0)
cv2.imshow('grey scale image',img)

cv2.imshow("Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

vals = img.flatten()
plt.hist(vals, bins = range(256))
plt.show()

ret,th1 = cv2.threshold(img,215,255,cv2.ADAPTIVE_THRESH_MEAN_C)
# th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
#             cv2.THRESH_BINARY,11,2)
# th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
#             cv2.THRESH_BINARY,11,2)
cv2.imshow("Image", th1)
cv2.waitKey(0)
cv2.destroyAllWindows()