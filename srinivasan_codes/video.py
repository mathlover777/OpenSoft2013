import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1 and cap!=None):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,20,20])
    upper_blue = np.array([130,255,255])
	
    lower_green = np.array([50,20,20])
    upper_green = np.array([70,255,255])
    edge=cv2.Canny(frame,100,200)
    blur = cv2.medianBlur(frame,5)
    img=cv2.imread('profile_pic.jpg')

	

    resize = cv2.resize(frame,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret,threshold = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    gray=cv2.GaussianBlur(gray,(5,5),0)
    thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
    kernel = np.ones((5,5),np.uint8)
    erosion = cv2.erode(thresh,kernel,iterations = 1)
    dilation = cv2.dilate(erosion,kernel,iterations = 1)

    # Threshold the HSV image to get only blue colors
    mask1 = cv2.inRange(hsv, lower_blue, upper_blue)
    mask2 = cv2.inRange(hsv, lower_green, upper_green)
	
    mask=cv2.bitwise_or(mask1,mask2);

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('edge',edge)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('resize',resize)
    cv2.imshow('threshold',threshold)
    cv2.imshow('gaussian threshold',thresh)
    cv2.imshow('blur',blur)
    cv2.imshow('erosion',erosion)
    cv2.imshow('dilation',dilation)
	
	
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()