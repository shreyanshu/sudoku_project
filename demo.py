import cv2

img = cv2.imread('try.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Over the Clouds", img)
cv2.imshow("Over the Clouds - gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
# ray = cv2.GaussianBlur(gray,(5,5),0)
# thresh = cv2.adaptiveThreshold(gray,255,1,1,11,2)
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# biggest = None
# max_area = 0
# for i in contours:
# 	area = cv2.contourArea(i)
#     if area > 100:
#     peri = cv2.arcLength(i,True)
#                 approx = cv2.approxPolyDP(i,0.02*peri,True)
#                 if area > max_area and len(approx)==4:
#                         biggest = approx
#                         max_area = area