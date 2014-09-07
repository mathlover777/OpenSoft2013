import numpy as np
def getTransformationMatrix(a,a1,b,b1,c,c1):
	# returns the exact transformation matrix
	# fails if a,b,c are co linear
	# assumes a... are 2d points
	# a.x a.y
	
def getTransformationMatrix(src,dst):
	# returns best fit rigid transformation matrix
	# fails if all of p1 are co linear
	return np.matrix(cv2.estimateRigidTransform(src, dst,False))

def transformMatrix(Trasform,TOld):
	# returns the new transformation matrix
	return Trasform * TOld

def mergeFragments(A,B,startA,endA,startB,endB):
	# merges two fragments
	# returns a new fragment


def constructImage(A):
	# creates an image for the final merged fragment
