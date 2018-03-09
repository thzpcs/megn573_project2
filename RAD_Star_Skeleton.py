# -*- coding: utf-8 -*-
"""
Spyder Editor

The objective is to implement the RAD representation to convert
all data instances in the folder Train into a single training
file rad d1, each line corresponding the RAD representation
of a data instance. Similarly, all instances in the folder Test
needs to be converted into a single testing file rad d1.t

"""

# Joints needed for encoding:
# 1: HipCenter
# 4: Head
# 8: HandLeft
# 12: HandRight
# 16: FootLeft
# 20: FootRight

import numpy
import os

rootDir = os.path.dirname(__file__) + '/dataset/train/' #<-- absolute dir the script is in



for subdir, dirs, files in os.walk(rootDir):
    for file in files:
        trainData = open(os.path.join(subdir, file), "r")
        print(os.path.join(subdir, file))
        
        for newLine in trainData:
            data = newLine.split()
            print(data[1])
        trainData.close()
        #print(os.path.join(subdir, file))
        
#f = open("months.txt")
#next = f.read(1)
#while next != "":
#    print(next)
#    next = f.read(1)