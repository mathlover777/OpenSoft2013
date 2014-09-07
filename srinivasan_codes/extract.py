import cv2
import numpy as np


image=cv2.imread('test/i1.png',0)
image=cv2.GaussianBlur(image,(5,5),10)
ret,threshold = cv2.threshold(image,245,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((5,5),np.uint8)
open=cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel)
corrected=cv2.morphologyEx(open, cv2.MORPH_CLOSE, kernel)
cv2.imshow('new_image',corrected)
contours, hierarchy = cv2.findContours(corrected,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

height,width= image.shape[:2]
contour_img=np.zeros((height,width,1), np.uint8)

contours=[cnt for cnt in contours if cv2.contourArea(cnt)>10000]

cv2.drawContours(contour_img, contours, -1, 255, 1)
canny=cv2.Canny(image,240,255)


# Repeated code for second image
image2=cv2.imread('test.jpg',0)
image2=cv2.GaussianBlur(image2,(5,5),10)
ret,threshold2 = cv2.threshold(image2,245,255,cv2.THRESH_BINARY_INV)
kernel2 = np.ones((5,5),np.uint8)
open2=cv2.morphologyEx(threshold2, cv2.MORPH_OPEN, kernel2)
corrected2=cv2.morphologyEx(open2, cv2.MORPH_CLOSE, kernel2)
cv2.imshow('new_image',corrected2)
contours2, hierarchy2 = cv2.findContours(corrected2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

height2,width2= image2.shape[:2]
contour_img2=np.zeros((height2,width2,1), np.uint8)

contours2=[cnt for cnt in contours2 if cv2.contourArea(cnt)>10000]

cv2.drawContours(contour_img2, contours2, -1, 255, 1)
cv2.imshow('contour_image2',contour_img2)
#End of Repeat


ret = cv2.matchShapes(contours[0],contours2[0],3,0.0)
print(ret)


cv2.imshow('original_image',image)
cv2.imshow('thresholded_image',threshold)
cv2.imshow('corrected_image',corrected)
cv2.imshow('canny_image',canny)
cv2.imshow('contour_image',contour_img)

k=cv2.waitKey(0)
if(k==27):
	cv2.destroyAllWindows()