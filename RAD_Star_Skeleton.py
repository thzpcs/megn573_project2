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

rootDir = os.path.dirname(__file__) + '/dataset/train/' #<-- absolute dir the script is in


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
#                alpha1.append(np.arctan2([hipCenter_y,head_y],[hipCenter_x,head_x])[1])
#                alpha2.append(np.arctan2([hipCenter_y,handLeft_y],[hipCenter_x,handLeft_x])[1])
#                alpha3.append(np.arctan2([hipCenter_y,footLeft_y],[hipCenter_x,footLeft_x])[1])
#                alpha4.append(np.arctan2([hipCenter_y,footRight_y],[hipCenter_x,footRight_x])[1])
#                alpha5.append(np.arctan2([hipCenter_y,handRight_y],[hipCenter_x,handRight_x])[1])
                
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
        

        dRange = (0, 0.75)
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
        
        radFile = open("rad_d1.t","w")
        
        radFile.write(str(rad_d1))
        radFile.close()
    
    
    ### Graphical Histogram plotting ###
    
    newd1 = pd.Series(d1)
    newd2 = pd.Series(d2)
    newd3 = pd.Series(d3)
    newd4 = pd.Series(d4)
    newd5 = pd.Series(d5)
    
    newTheta1 = pd.Series(theta1)
    newTheta2 = pd.Series(theta2)
    newTheta3 = pd.Series(theta3)
    newTheta4 = pd.Series(theta4)
    newtheta5 = pd.Series(theta5)
    
    num_bins = nBins
    
    dFig = plt.figure(figsize=(10, 10))
    thetaFig = plt.figure(figsize=(10, 10))
    
    dFig.suptitle('d Value Histograms', fontsize = 14)
    thetaFig.suptitle('Theta Value Histograms', fontsize = 14)
    
    ## d plots
    
    dx1 = dFig.add_subplot(5, 1, 1)
    dx2 = dFig.add_subplot(5, 1, 2)
    dx3 = dFig.add_subplot(5, 1, 3)
    dx4 = dFig.add_subplot(5, 1, 4)
    dx5 = dFig.add_subplot(5, 1, 5)
    
    n, bins, patches = dx1.hist(newd1.dropna(), num_bins, facecolor='blue', alpha = 0.5)
    dx1.set_xlabel('Values')
    dx1.set_ylabel('d1 Frequency')
    
    n, bins, patches = dx2.hist(newd2.dropna(), num_bins, facecolor='blue', alpha = 0.5)
    dx2.set_xlabel('Values')
    dx2.set_ylabel('d2 Frequency')
    
    n, bins, patches = dx3.hist(newd3.dropna(), num_bins, facecolor='blue', alpha = 0.5)
    dx3.set_xlabel('Values')
    dx3.set_ylabel('d3 Frequency')
    
    n, bins, patches = dx4.hist(newd4.dropna(), num_bins, facecolor='blue', alpha = 0.5)
    dx4.set_xlabel('Values')
    dx4.set_ylabel('d4 Frequency')
    
    n, bins, patches = dx5.hist(newd5.dropna(), num_bins, facecolor='blue', alpha = 0.5)
    dx5.set_xlabel('Values')
    dx5.set_ylabel('d5 Frequency')

    ## Theta plots
    
    thetaX1 = thetaFig.add_subplot(5, 1, 1)
    thetaX2 = thetaFig.add_subplot(5, 1, 2)
    thetaX3 = thetaFig.add_subplot(5, 1, 3)
    thetaX4 = thetaFig.add_subplot(5, 1, 4)
    thetaX5 = thetaFig.add_subplot(5, 1, 5)
    
    n, bins, patches = thetaX1.hist(newd1.dropna(), num_bins, facecolor='blue', alpha = 0.5)
    thetaX1.set_xlabel('Values')
    thetaX1.set_ylabel('Theta 1 Frequency')
    
    n, bins, patches = thetaX2.hist(newd2.dropna(), num_bins, facecolor='blue', alpha = 0.5)
    thetaX2.set_xlabel('Values')
    thetaX2.set_ylabel('Theta 2 Frequency')
    
    n, bins, patches = thetaX3.hist(newd3.dropna(), num_bins, facecolor='blue', alpha = 0.5)
    thetaX3.set_xlabel('Values')
    thetaX3.set_ylabel('Theta 3 Frequency')
    
    n, bins, patches = thetaX4.hist(newd4.dropna(), num_bins, facecolor='blue', alpha = 0.5)
    thetaX4.set_xlabel('Values')
    thetaX4.set_ylabel('Theta 4 Frequency')
    
    n, bins, patches = thetaX5.hist(newd5.dropna(), num_bins, facecolor='blue', alpha = 0.5)
    thetaX5.set_xlabel('Values')
    thetaX5.set_ylabel('Theta 5 Frequency')
    
    plt.show()
        

        
