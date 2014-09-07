#!/usr/bin/python

import sys
import math
import cv2
import numpy as np
import random
import config
from Fragment import *

def reservoirSample(A,B,n,k):
	# tested
	# reservoir sampling without sorting n = A.size k = B.size
	# print "IN RESERVOIR n = ",n,"k=",k
	for i in range(0,k):
		B[i] = A[i]
	for i in range(k,n):
		j = random.randint(1,i)
		if(j < k):
			B[j] = A[i]
	return

def selectNfromM(A,B,n,k):
	separation = (n*1.0)/(k*1.0)
	# print "\nseparation = ",separation
	index = 0
	for i in range(0,k):
		if(index>=n):
			index = n-1
		B[i] = A[index]
		nextIndex = separation * i
		if(nextIndex == index):
			nextIndex = nextIndex + 1
		index = nextIndex
	return

def test():
	m = 13
	n = 100
	reservoir = np.arange(m)
	sample = np.arange(n)
	uniform = np.arange(n)
	# reservoirSample(reservoir,sample,m,n)
	selectNfromM(reservoir,uniform,m,n)
	
	print "\nRESERVOIR:\n",reservoir
	# print "\nSAMPLE:\n",sample
	# sample.sort()
	# print "\nSAMPLE SORTED:\n",sample
	print "\nUNIFORM:\n",uniform
	return

def getFileName(filename):
	imagepathlist = []
	file = open(filename)
	while 1:
	    line = file.readline()
	    print line
	    if not line:
		break
	    pass # do something
	return imagepathlist

def testReadFromFile():
	cmd = sys.argv[1:]
	filename = cmd[0]
	print "FILENAME = ",filename
	imglist = getFileName(filename)
	print imglist
	return

def main():
	# test()
	testReadFromFile()
	return

if __name__ == "__main__":
    main()