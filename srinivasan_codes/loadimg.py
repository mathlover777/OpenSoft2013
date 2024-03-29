import cv2
import numpy as np
from matplotlib import pyplot as plot

img=cv2.imread('profile_pic.jpg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
	cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
	cv2.imwrite('messigray.png',img)
cv2.destroyAllWindows()

plot.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plot.xticks([0]), plot.yticks([0])  # to hide tick values on X and Y axis
plot.show()


def nothing(x):
	pass

# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)

while(1):
	cv2.imshow('image',img)
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break

	# get current positions of four trackbars
	r = cv2.getTrackbarPos('R','image')
	g = cv2.getTrackbarPos('G','image')
	b = cv2.getTrackbarPos('B','image')
	s = cv2.getTrackbarPos(switch,'image')

	if s == 0:
		img[:] = 0
	else:
		img[:] = [b,g,r]

cv2.destroyAllWindows()


# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv2.line(img,(0,0),(511,511),(255,0,0),5)
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv2.circle(img,(447,63), 63, (0,0,255), -1)
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

cv2.imshow('image',img)


k = cv2.waitKey(0) & 0xFF
if k == 27:
	cv2.destroyAllWindows()



# mouse callback function
def draw_circle(event,x,y,flags,param):
	if event == cv2.EVENT_LBUTTONDBLCLK:
		cv2.circle(img,(x,y),100,(255,0,0),-1)

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
	cv2.imshow('image',img)
	if cv2.waitKey(20) & 0xFF == 27:
		break
cv2.destroyAllWindows()



drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
jx,jy = -1,-1

# mouse callback function
def draw_circle(event,x,y,flags,param):
	global ix,iy,drawing,mode

	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		ix,iy = x,y

	elif event == cv2.EVENT_MOUSEMOVE:

		jx,jy = x,y
		if drawing == True:
			if mode == True:
				cv2.rectangle(img,(ix,iy),(jx,jy),(0,0,0),-1)
				cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),1)
			else:
				cv2.circle(img,(x,y),5,(0,0,255),-1)

	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False
		if mode == True:
			cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),1)
		else:
			cv2.circle(img,(x,y),5,(0,0,255),-1)

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
	cv2.imshow('image',img)
	k = cv2.waitKey(1) & 0xFF
	if k == ord('m'):
		mode = not mode
	elif k == 27:
		break

cv2.destroyAllWindows()

e1 = cv2.getTickCount()
# your code execution
e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()


img1 = cv2.imread('profile_pic.jpg')

e1 = cv2.getTickCount()
for i in xrange(5,49,2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print t

res = cv2.medianBlur(img,49)

cv2.imshow('image',img1)
k=cv2.waitKey(0) & 0xFF
if k==27:
	cv2.destroyAllWindows()
	

