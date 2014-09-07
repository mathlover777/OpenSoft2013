#!/usr/bin/python
import sys
import math
import cv2
import numpy as np

NORMALNUMPY = 1

def iround(x):
	# """iround(number) -> integer
	# Round a number to the nearest integer."""
	return int(round(x) - .5) + (x > 0)

def getTransformedPoint(T,P):
	# tested
	X = np.matrix([[0],[0],[1]])
	X[0] = P[0]
	X[1] = P[1]
	# print X
	Y = T * X
	# print Y
	if((Y[2]-1)>.000001):
		print "WARNING:Value!=1 in 3rd homogeneous dimension"
	Y[2] = 1
	Q =  np.squeeze(np.asarray(Y))
	Q = [iround(Q[0]),iround(Q[1])]
	return Q

def twoD_to_ThreeD_Affine(T):
	# tested
	A = np.matrix([[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]])
	A[0,0] = T[0,0]
	A[0,1] = T[0,1]
	A[0,2] = T[0,2]
	A[1,0] = T[1,0]
	A[1,1] = T[1,1]
	A[1,2] = T[1,2]
	A[2,0] = 0.0
	A[2,1] = 0.0
	A[2,2] = 1.0
	return A

def threeD_to_TwoD_Affine(T):
	# tested
	A = np.matrix([[0.0,0.0,0.0],[0.0,0.0,0.0]])
	A[0,0] = T[0,0]
	A[0,1] = T[0,1]
	A[0,2] = T[0,2]
	A[1,0] = T[1,0]
	A[1,1] = T[1,1]
	A[1,2] = T[1,2]
	return A

def getSampleTransformationMatrix(theta,tx,ty):
	Rot = np.matrix([[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]])
	Tran = np.matrix([[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]])

	Tran[0,0] = Tran[1,1] = Tran[2,2] = 1
	Tran[0,2] = tx
	Tran[1,2] = ty

	Rot[0,0] = math.cos(theta)
	Rot[0,1] = math.sin(theta)
	Rot[1,0] = -1.0 * math.sin(theta)
	Rot[1,1] = math.cos(theta)
	Rot[2,2] = 1.0

	return Tran * Rot

def testbasic():
	# basic testing to get numpy - cv 2
	# YPEE WORKING !!
	A = np.empty([1,6,2],np.int)
	A[0][0] = [100,40]
	A[0][1] = [110,40]
	A[0][2] = [120,30]
	A[0][3] = [130,20]
	A[0][4] = [140,10]
	A[0][5] = [140,0]

	# print A[0][0][0],A[0][0][1]
	
	source = np.zeros((400,400,1),np.uint8)
	dest = np.zeros((400,400,1),np.uint8)

	print A
	B = A + np.array([40,50]).astype(np.int)
	print B

	cv2.drawContours(source,A,-1,255,1)
	cv2.drawContours(dest,B,-1,255,1)

	# cv2.imshow("SOURCE",source)
	# cv2.imshow("DEST",dest)

	T = cv2.estimateRigidTransform(A,B,False)
	print T

	T3 = twoD_to_ThreeD_Affine(T)
	print T3

	print getTransformedPoint(T3,A[0][4])
	# print threeD_to_TwoD_Affine(T3)

	# print getTransformedPoint(T,A[0][5])
	# H = np.empty((3,3))
	# cv.FindHomography(A,B, H, method=cv.CV_RANSAC, ransacReprojThreshold=3.0, status=None)
	# print H

	# k=cv2.waitKey(0)
	# if(k==27):
	# 	cv2.destroyAllWindows()

	return

def getTransformationMatrixFromArray(A,B):
	# A,B both have to be numpy array
	# they must contain same number of points say n
	# so shape of A,B = [1,n,2]
	# returns a 3*3 np.matrix and a success flag(=1->OH yeah , 0 ->:())
	T = cv2.estimateRigidTransform(A,B,False)
	return twoD_to_ThreeD_Affine(T)

def transformCountour(C,T,flag):
	# Tested for numpy array
	# transforms the contour C with transformation matrix 
	# changes are applied on C,,, no new contour is created
	# C is assumed in this shape [1,n,2] ... where n is the number of points
	# on the contour
	if(flag == NORMALNUMPY):
		(dummy1,n,dummy2) = C.shape
		for i in range(0,n):
			C[0][i] = getTransformedPoint(T,C[0][i])
		return

def test_transformCountour():
	n = 5
	shape = (1,n,2)
	A = np.random.randint(0, 200, shape).astype(np.int)
	B = np.random.randint(0, 200, shape).astype(np.int)
	for i in range(0,n):
		B[0][i] = A[0][i]

	source = np.zeros((400,400,1),np.uint8)
	cv2.drawContours(source,A,-1,255,1)
	cv2.imshow("SOURCE",source)

	T = getSampleTransformationMatrix(-math.pi/4,100,200)
	print T

	transformCountour(B,T,NORMALNUMPY)
	# print B

	dest = np.zeros((400,400,1),np.uint8)
	cv2.drawContours(dest,B,-1,255,1)
	cv2.imshow("DEST",dest)	

	T1 = getTransformationMatrixFromArray(A,B)
	print T1

	for i in range(0,n):
		B[0][i] = A[0][i]	

	sourceTodest = np.zeros((400,400,1),np.uint8)
	transformCountour(B,T1,NORMALNUMPY)
	cv2.drawContours(sourceTodest,B,-1,255,1)
	cv2.imshow("SourceToDest",sourceTodest)

	T2 = getTransformationMatrixFromArray(B,A)
	# print T1.getI()
	print T2
	destToSource = np.zeros((400,400,1),np.uint8)
	transformCountour(B,T2,NORMALNUMPY)
	print A
	print B
	cv2.drawContours(destToSource,B,-1,255,1)
	cv2.imshow("DestToSource",destToSource)


	k=cv2.waitKey(0)
	if(k==27):
		cv2.destroyAllWindows()
	return

def testnumpyMat():
	A = np.matrix([[0,0,0],[0,0,0],[0,0,0]])
	A.fill(0)
	print A
	B = np.matrix([[0,0,0],[0,0,0],[0,0,0]])
	B.fill(0)
	B[0,0] = 1
	B[1,1] = 2
	B[2,2] = 3
	print B
	C = A + B
	print C
	D = C.getI()
	E = np.matrix([[1],[2],[1]])
	print D
	print D * E
	return

def getTransformationMatirxFromFragment(A,B,startA,endA,startB,endB):
	# MAY FAIL if transformation is not feasible entirely or all the points are on straight line need to resolve
	# Here A and B are Fragments
	# startA and endA are points on A and same for B
	# B have to be moved such that startB --> startA endB --> endB
	# na = |endA - startA|+1 nb = |endB - startB|+1
	# if na!=nb we will do a reservoir sampling on the larger one
	# to make both the contours of the same size say n
	# next numpy arrays of shape (1,n,2) are created and the transformation is computed
	return
def main():
	# testbasic()
	test_transformCountour()
	# testnumpyMat()
	return

if __name__ == "__main__":
	main()