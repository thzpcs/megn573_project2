# -*- coding: utf-8 -*-
"""
Spyder Editor

Written by Skyler Morris for MEGN 573 at the Colorado School of Mines

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

import numpy as np
import os


rootDir = os.path.dirname(__file__) + '/dataset/train/' #<-- absolute dir the script is in
i = 0



# loops through each file in the /dataset/ directory, and reads the data from each line.

for subdir, dirs, files in os.walk(rootDir):
    for file in files:
        trainData = open(os.path.join(subdir, file), "r")

        numLines = sum(1 for line in open(os.path.join(subdir, file)))
        
        # Initializes d_arrays
        d1 = np.zeros(numLines)
        d2 = np.zeros(numLines)
        d3 = np.zeros(numLines)
        d4 = np.zeros(numLines)
        d5 = np.zeros(numLines)
        #
        #
        # theta1 is d1 --> d2
        # theta2 is d2 --> d3
        # theta3 is d3 --> d4
        # theta4 is d4 --> d5
        # theta5 is d5 --> d1
        # 
        # Initializes theta arrays
        theta1 = np.zeros(numLines)
        theta2 = np.zeros(numLines)
        theta3 = np.zeros(numLines)
        theta4 = np.zeros(numLines)
        theta5 = np.zeros(numLines)
        
        for newLine in trainData:
            data = newLine.split()
            data = [float(i) for i in data]
           # print(data[1])
        
        # Checks the values of the first column in each line, and matches them 
        # to the specific joints, with x, y, and z position 

            if data[1] == 1:
                hipCenter_x = data[2]
                hipCenter_y = data[3]
                hipCenter_z = data[4]
                
            elif data[1] == 4:
                head_x = data[2]
                head_y = data[3]
                head_z = data[4]
                
            elif data[1] == 8:
                handLeft_x = data[2]
                handLeft_y = data[3]
                handLeft_z = data[4]
            
            elif data[1] == 12:
                handRight_x = data[2]
                handRight_y = data[3]
                handRight_z = data[4]
                
            elif data[1] == 16:
                footLeft_x = data[2]
                footLeft_y = data[3]
                footLeft_z = data[4]
                
            elif data[1] == 20:
                footRight_x = data[2]
                footRight_y = data[3]
                footRight_z = data[4]
            
            
        # Calculates the d and theta values for each limb
        # Reading clockwise:
        # d1 is HipCenter --> head
        # d2 is HipCenter --> leftHand
        # d3 is HipCenter --> leftFoot
        # d4 is HipCenter --> rightFoot
        # d5 is HipCenter --> rightHand
        #
        
        
        
        d1[i] = np.sqrt((hipCenter_x-head_x)**2+(hipCenter_y-head_y)**2)
        d2[i] = np.sqrt((hipCenter_x-handLeft_x)**2+(hipCenter_y-handLeft_y)**2)
        d3[i] = np.sqrt((hipCenter_x-handRight_x)**2+(hipCenter_y-handRight_y)**2)
        d4[i] = np.sqrt((hipCenter_x-footLeft_x)**2+(hipCenter_y-footLeft_y)**2)
        d5[i] = np.sqrt((hipCenter_x-footRight_x)**2+(hipCenter_y-footRight_y)**2)
        
        theta1[i] = np.arctan2([hipCenter_y,head_y],[hipCenter_x,head_x])[1]
        theta2[i] = np.arctan2([hipCenter_y,head_y],[hipCenter_x,head_x])[1]
        theta3[i] = np.arctan2([hipCenter_y,head_y],[hipCenter_x,head_x])[1]
        theta4[i] = np.arctan2([hipCenter_y,head_y],[hipCenter_x,head_x])[1]
        theta5[i] = np.arctan2([hipCenter_y,head_y],[hipCenter_x,head_x])[1]
        
        
        i += 1
    trainData.close()
        

        
