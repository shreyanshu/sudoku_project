import cv2
import numpy as np 
import matplotlib.pyplot as plt 


img = cv2.imread("try1.jpg",0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('grayscale.png', img)

