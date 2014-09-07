#!/usr/bin/python
import numpy as np
import cv2

def main():
	shape = (1, 10, 2) # Needs to be a 3D array
	source = np.random.randint(0, 100, shape).astype(np.int)
	target = source + np.array([1, 0]).astype(np.int)
	print source
	print source.shape
	print source.dtype
	print source.itemsize
	print source.ndim
	
	print target.shape
	transformation = cv2.estimateRigidTransform(source, target, False)
	print transformation
	return

if __name__ == "__main__":
    main()