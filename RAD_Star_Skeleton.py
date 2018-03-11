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
import pandas as pd
import matplotlib.pyplot as plt



def RAD(filePath):
    
    rootDir = os.path.dirname(__file__) + '/dataset' + filePath #<-- absolute dir the script is in
    
    # Initializes d_arrays
    #
    d1 = []
    d2 = []
    d3 = []
    d4 = []
    d5 = []
    #
    # Initializes theta arrays
    #
    theta1 = []
    theta2 = []
    theta3 = []
    theta4 = []
    theta5 = []
    
    # Starting index for arrays. Each index is a frame (ie d1[1] = d1 for frame 1)
    i = 0
    
    # loops through each file in the /dataset/ directory, and reads the data from each line.
    
    for subdir, dirs, files in os.walk(rootDir):
        for file in files:
            trainData = open(os.path.join(subdir, file), "r")
    
            #numLines = sum(1 for line in open(os.path.join(subdir, file)))
            
            
            for newLine in trainData:
                data = newLine.split()
                data = [float(i) for i in data]
            
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
                
                    # Calculates the d and theta values for each limb and adds them
                    # to the array for that value
                    #
                    # Reading clockwise:
                    # d1 is HipCenter --> head
                    # d2 is HipCenter --> leftHand
                    # d3 is HipCenter --> leftFoot
                    # d4 is HipCenter --> rightFoot
                    # d5 is HipCenter --> rightHand
                    #
                    # theta1 is d1 --> d2
                    # theta2 is d2 --> d3
                    # theta3 is d3 --> d4
                    # theta4 is d4 --> d5
                    # theta5 is d5 --> d1
                    # 
            
            
                    ### RAD Calculations ###
                    d1.append(np.sqrt((hipCenter_x-head_x)**2+(hipCenter_y-head_y)**2))
                    d2.append(np.sqrt((hipCenter_x-handLeft_x)**2+(hipCenter_y-handLeft_y)**2))
                    d3.append(np.sqrt((hipCenter_x-handRight_x)**2+(hipCenter_y-handRight_y)**2))
                    d4.append(np.sqrt((hipCenter_x-footLeft_x)**2+(hipCenter_y-footLeft_y)**2))
                    d5.append(np.sqrt((hipCenter_x-footRight_x)**2+(hipCenter_y-footRight_y)**2))
                    
                    # Alpha values are absolute values for each angle from the x-axis
                    
                    alpha1 = np.arctan2((hipCenter_y-head_y), (hipCenter_x-head_x))
                    alpha2 = np.arctan2((hipCenter_y-handLeft_y), (hipCenter_x-handLeft_x))
                    alpha3 = np.arctan2((hipCenter_y-footLeft_y), (hipCenter_x-footLeft_x))
                    alpha4 = np.arctan2((hipCenter_y-footRight_y), (hipCenter_x-footRight_x))
                    alpha5 = np.arctan2((hipCenter_y-handRight_y), (hipCenter_x-handRight_x))
                    
                    theta1.append(abs(alpha1-alpha2))
                    theta2.append(abs(alpha2-alpha3))
                    theta3.append(abs(alpha3-alpha4))
                    theta4.append(abs(alpha4-alpha5))
                    theta5.append(abs(alpha5-alpha1))
                    
                    i += 1
                    
            trainData.close()
            
            ## Histogram Calculations
            
    
            dRange = (0, 1)
            thetaRange = (0.0,np.pi)
            
            # Calculates the normalized d histograms, number of bins is determined 
            # by the 'auto' flag, which is the maximum of the ‘sturges’ and ‘fd’ estimators. 
            # See the Numpy documentation at scipy.org for more information
            
            histD1 = np.histogram(d1, bins='auto', range= dRange, normed = 'True')
            
            # Uses the largest number of bins (d1), which determines the bins for all other dHist
            nBins = len(histD1[0])
            
            histD2 = np.histogram(d2, bins=nBins, range= dRange, normed = 'True')
            histD3 = np.histogram(d3, bins=nBins, range= dRange, normed = 'True')
            histD4 = np.histogram(d4, bins=nBins, range= dRange, normed = 'True')
            histD5 = np.histogram(d5, bins=nBins, range= dRange, normed = 'True')
                    
            histTheta1 = np.histogram(theta1, bins='auto', range= thetaRange, normed = 'True')
            
            mBins = len(histTheta1[0])
            
            histTheta2 = np.histogram(theta2, bins=mBins, range= thetaRange, normed = 'True')
            histTheta3 = np.histogram(theta3, bins=mBins, range= thetaRange, normed = 'True')
            histTheta4 = np.histogram(theta4, bins=mBins, range= thetaRange, normed = 'True')
            histTheta5 = np.histogram(theta5, bins=mBins, range= thetaRange, normed = 'True')
            
            rad_d1 = np.hstack([histD1[0], histD2[0], histD3[0], histD4[0], histD5[0],  \
            histTheta1[0], histTheta2[0], histTheta3[0], histTheta4[0], histTheta5[0]])
        
            
            ## Creates the file for saving the histogram
            
        return(rad_d1);
            
        
        
### Function calls for test and training functions
            
# Training function

radTrain = RAD('/train/')
np.savetxt("rad_d1", radTrain, fmt='%f')

# Testing function

radTest = RAD('/test/')
np.savetxt("rad_d1.t", radTest, fmt='%1.4f')   
            

            
    
        

        
