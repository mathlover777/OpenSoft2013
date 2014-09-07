import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1 and cap!=None):
	
	_,frame=cap.read()
	frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	gaussian=cv2.GaussianBlur(frame,(5,5),3)
	canny=cv2.Canny(frame,70,255)
	sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
	sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
	thresh = cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
	contours, hierarchy = cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	image=frame
	#cv2.drawContours(frame, contours, -1, (0,255,0), 1)
	
	for cnt in contours:
		epsilon = 0.01*cv2.arcLength(cnt,True)
		approx = cv2.approxPolyDP(cnt,epsilon,True)
		cv2.drawContours(image, approx, -1, (0,255,0), 1)
	
	
	cv2.imshow('gaussian',gaussian)
	cv2.imshow('image',image)
	cv2.imshow('frame',frame)
	cv2.imshow('canny',canny)
	cv2.imshow('sobelx',sobelx)
	cv2.imshow('sobely',sobely)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
	

cv2.destroyAllWindows()