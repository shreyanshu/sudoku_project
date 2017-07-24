import cv2
import numpy as np

def rectify(h):
	''' this function put vertices of square we got, in clockwise order '''
	h = h.reshape(4,2)
	# print(h)
	hnew = np.zeros((4,2),dtype = np.float32)
	add = h.sum(1)
	hnew[0] = h[np.argmin(add)]
	hnew[2] = h[np.argmax(add)]
	diff = np.diff(h,axis = 1)
	hnew[1] = h[np.argmin(diff)]
	hnew[3] = h[np.argmax(diff)]
	# print(hnew)
	return hnew

img = cv2.imread('sudoku.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(gray, 255, 1, 1, 5, 2)
imga, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
image_area = gray.size	# this is area of the image

for i in contours:
    # if cv2.contourArea(i)> image_area/2:
        # if area of box > half of image area, it is possibly the biggest blob
        # peri = cv2.arcLength(i,True)
	# approx = cv2.approxPolyDP(i,0.02,True)
	cv2.drawContours(img, [i], 0, (0,255,0), 2)
	cv2.imshow('image',img)
	# cv2.waitKey(0)
        # break
cv2.waitKey(0)

# h = np.array([ [0,0],[449,0],[449,449],[0,449] ],np.float32)
# # print(h)	# this is corners of new square image taken in CW order
# approx=rectify(approx)	# we put the corners of biggest square in CW order to match with h
# retval = cv2.getPerspectiveTransform(approx,h)	# apply perspective transformation matrix
# warp = cv2.warpPerspective(img,retval,(450,450))  # Now we get perfect square with size 450x450
# # cv2.imshow('image',warp)
# # cv2.waitKey(0)
# warpg = cv2.cvtColor(warp,cv2.COLOR_BGR2GRAY)
# # cv2.imshow('s',warpg)
# # cv2.waitKey(0)

# sudo = np.zeros((9,9),np.uint8)	

# smooth = cv2.GaussianBlur(warpg,(3,3),3)
# thresh = cv2.adaptiveThreshold(smooth,255,0,1,5,2)
# kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
# erode = cv2.erode(thresh,kernel,iterations =1)
# dilate =cv2.dilate(erode,kernel,iterations =1)
# im, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# # cv2.imshow("", thresh)
# # cv2.waitKey(0)

# # for cnt in contours:
