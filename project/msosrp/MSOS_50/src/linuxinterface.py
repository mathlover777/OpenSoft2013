#!/usr/bin/python
import sys
from Match import *

def getFileList():
	# print sys.argv
    n = len(sys.argv)
    if(n<2 or n>2):
        print "USAGE : ./linuxinterface.py filename"
        return None
    print "\nINPUT FILE NAME = {",sys.argv[1],"}"
    file = open(sys.argv[1])
    List = []
    while 1:
        line = file.readline()
        if not line:
            break
        if(line[-1:] == "\n"):
            line = line[:-1]
        if(line == ""):
            continue
        List.append(line)
    return List

def main():
    List = getFileList()
    for i in range(0,len(List)):
        print "\nIMAGE [",(i+1),"] = {",List[i],"}"
    execute(List)
    return

if __name__ == "__main__":
    main()