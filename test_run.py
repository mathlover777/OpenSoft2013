import cv2
import numpy as np
import math
from smith_waterman import *

n_img=4

image=[None for i in range(0,n_img)]
corrected=[None for i in range(0,n_img)]
kernel = np.ones((5,5),np.uint8)
contours=[None for i in range(0,n_img)]
contour_img=[None for i in range(0,n_img)]
cont=[None for i in range(0,n_img)]
turning=[[] for i in range(0,n_img)]
turn_pts=[[] for i in range(0,n_img)]

for i in range(1,n_img):
	image[i]=cv2.imread('test4/i'+str(i)+'.jpg',0)
	image[i]=cv2.GaussianBlur(image[i],(5,5),3)
	
	ret,threshold = cv2.threshold(image[i],249,255,cv2.THRESH_BINARY_INV)
	open=cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel)
	corrected[i]=cv2.morphologyEx(open, cv2.MORPH_CLOSE, kernel)
	
	#cv2.imshow('image'+str(i),corrected[i])
	
	contours[i], hierarchy = cv2.findContours(corrected[i],cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	
	
	height,width= image[i].shape[:2]
	contour_img[i]=np.zeros((height,width,1), np.uint8)
	
	contours[i]=[cnt for cnt in contours[i] if cv2.contourArea(cnt)>50000]
	'''cont[i]=[]
	[cont[i].append(el) for el in contours[i]] 
	print(cont[i])'''
	
	cv2.drawContours(contour_img[i], contours[i], -1, 255, 1)
	cont[i]=cv2.approxPolyDP(contours[i][0],2,True)
	cv2.drawContours(contour_img[i], cont[i], -1, 255, 1)
	
	for num in range(1,len(contours[i][0])-1):
		vector1=contours[i][0][num-1][0]-contours[i][0][num][0]
		vector2=contours[i][0][num+1][0]-contours[i][0][num][0]
		#print(cont[i][num][0])
		#print(cont[i][num-1][0])
		#print(vector1)
		
		cos=(vector1[0]*vector2[0]+vector1[1]*vector2[1])/(math.sqrt((math.pow(vector1[0],2)+math.pow(vector1[1],2))*(math.pow(vector2[0],2)+math.pow(vector2[1],2))))
		turn=round(math.acos(cos),100)
		if abs(turn)>=(10*3.14/180) and (abs(turn)<=(170*3.14/180) or abs(turn)>=(190*3.14/180)):
			turning[i].append(turn)
			turn_pts[i].append(contours[i][0][num])
		
		

	#print(turning)
		
	
	'''cont[i]=contours[i][0]
	for k in range(1,len(contours[i])):
		cont[i]=cv2.bitwise_and(cont[i],contours[i][k]);
		'''
	cv2.imshow('contour_image'+str(i),contour_img[i])

for i in range(1,n_img):
	for j in range(1,n_img):
		ret = cv2.matchShapes(cont[i],cont[j],3,0.0)
		#print(str(i)+" , "+str(j)+" , RET = "+str(ret))

#print(cont[i])
for i in range(1,n_img):
	for j in range(1,n_img):
		print("For Image "+str(i)+" and Image "+str(j));
		if i==3 and j==2:
			print("Printed for "+str(i)+str(j))
			start(turning[i],turning[j][::-1],turn_pts[i],turn_pts[j][::-1],height,width)
	
k=cv2.waitKey(0)
if(k==27):
	cv2.destroyAllWindows()