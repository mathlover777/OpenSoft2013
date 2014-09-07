import numpy as np
import math
import cv2


space=-1000
match=5
mismatch=-200
isInitialized=False
scoreTable=[]
sequence1=""
sequence2=""

class Cell:
	prevCell=None
	score=0
	row=0
	col=0
		
	def __init__(self,row=0,col=0,score=0):
		self.row=row
		self.col=col
		self.score=score
		

highScoreCell=Cell()
	


def getInitialScore(row,col):
   return 0

def getInitialPointer(row,col):
   return None


def initialize(length1,length2):
	global scoreTable,isInitialized,highScoreCell
	scoreTable = [[0 for x in range(0,length2)] for y in range(0,length1)] 
	for i in range(0,length1):
		for j in range(0,length2):
			scoreTable[i][j] = Cell(i,j);
	initializeScores(length1,length2);
	initializePointers(length1,length2);
	highScoreCell=Cell()

	isInitialized = True;

def initializeScores(length1,length2):
	global scoreTable
	for i in range(0,length1):
		for j in range(0,length2):
			scoreTable[i][j].score=getInitialScore(i, j);
		 

def initializePointers(length1,length2):
	global scoreTable
	for i in range(0,length1):
		for j in range(0,length2):
			scoreTable[i][j].prevCell=getInitialPointer(i, j);


def fillInCell(currentCell, cellAbove, cellToLeft, cellAboveLeft):
	global space,match,mismatch,scoreTable,sequence1,sequence2,highScoreCell
	rowSpaceScore = cellAbove.score + space
	colSpaceScore = cellToLeft.score + space
	matchOrMismatchScore = cellAboveLeft.score
	if(abs(sequence1[currentCell.row - 1] - sequence2[currentCell.col - 1])<(0.01*3.14/180)):
		matchOrMismatchScore += match;
	else:
		matchOrMismatchScore += mismatch;
		
	if(rowSpaceScore >= colSpaceScore):
		if(matchOrMismatchScore >= rowSpaceScore):
			if(matchOrMismatchScore > 0):
				currentCell.score=matchOrMismatchScore;
				currentCell.prevCell=cellAboveLeft;
		else:
			if(rowSpaceScore > 0):
				currentCell.score=rowSpaceScore;
				currentCell.prevCell=cellAbove;
	else:
		if(matchOrMismatchScore >= colSpaceScore):
			if(matchOrMismatchScore > 0):
				currentCell.score=matchOrMismatchScore;
				currentCell.prevCell=cellAboveLeft;
		else:
			if(colSpaceScore > 0):
				currentCell.score=colSpaceScore;
				currentCell.prevCell=cellToLeft;
	if(currentCell.score > highScoreCell.score):
		highScoreCell = currentCell;
		


def traceBackIsNotDone(currentCell):
	return currentCell.getScore() != 0;

def getTracebackStartingCell():
	return highScoreCell;


def fillIn(length1,length2):
	for row in range(1,len(scoreTable)):
		for col in range(1,len(scoreTable[row])):
			currentCell = scoreTable[row][col];
			cellAbove = scoreTable[row - 1][col];
			cellToLeft = scoreTable[row][col - 1];
			cellAboveLeft = scoreTable[row - 1][col - 1];
			fillInCell(currentCell, cellAbove, cellToLeft, cellAboveLeft);
			
			
traceBack=[]
traceBack1=[]
def start(seq1,seq2,track,track1,height,width):
	global sequence1,sequence2,scoreTable,traceBack,traceBack1
	sequence1=seq1
	sequence2=seq2
	l1=len(sequence1)+1
	l2=len(sequence2)+1
	initialize(l1,l2)
	fillIn(l1,l2)
	'''for i in scoreTable:
		print((' ').join([str(j.score) for j in i]))
		print '\n'

	cell=highScoreCell
	
	while cell.score!=0:
		print(cell.score)
		cell=cell.prevCell'''
	
	print(highScoreCell.score)
	contour_img=np.zeros((height,width,1), np.uint8)
	contour_img1=np.zeros((height,width,1), np.uint8)
	contour_img2=np.zeros((height,width,1), np.uint8)
	contour_img3=np.zeros((height,width,1), np.uint8)
	getTraceback(track,track1,seq1,seq2)
	#traceBack=cv2.approxPolyDP(traceBack,2,True)
	cv2.drawContours(contour_img, traceBack, -1, 255, 1)
	cv2.drawContours(contour_img1, track, -1, 255, 1)
	cv2.drawContours(contour_img2, traceBack1, -1, 255, 1)
	cv2.drawContours(contour_img3, track1, -1, 255, 1)
	
	cv2.imshow('IMPORTANT !!! :D',contour_img)
	cv2.imshow('IMPORTANT2 !!! :D',contour_img1)
	cv2.imshow('IMPORTANT1 !!! :D',contour_img2)
	cv2.imshow('IMPORTANT12 !!! :D',contour_img3)
	

#start()

def getTraceback(track,track1,s1,s2):
	global traceBack,traceBack1,highScoreCell
	traceBack=[]
	cell=highScoreCell
	while(cell.score!=0):
		row=cell.row-1
		col=cell.col-1
		#print(s1[row])
		#print(s2[col])
		traceBack.append(track[row])
		traceBack1.append(track1[col])
		cell=cell.prevCell
		
	