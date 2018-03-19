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


def RAD(filePath):
    
    rootDir = os.path.dirname(__file__) + '/dataset/' + filePath #<-- absolute dir the script is in
    
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
    frame = 0
    rad_d1 = [0]*250
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
                    
                    frame += 1
                    
                    
                    ## Histogram Calculations
                    dRange = (0, 1)
                    thetaRange = (0.0,np.pi)
                    
                    # Calculates the normalized d histograms, number of bins is determined 
                    # by the 'auto' flag, which is the maximum of the ‘sturges’ and ‘fd’ estimators. 
                    # See the Numpy documentation at scipy.org for more information
                    
                    histD1 = np.histogram(d1, bins=35, range= dRange, normed = 'True')
                    
                    # Uses the largest number of bins (d1), which determines the bins for all other dHist
                    nBins = len(histD1[0])
                    
                    histD2 = np.histogram(d2, bins=nBins, range= dRange, normed = 'True')
                    histD3 = np.histogram(d3, bins=nBins, range= dRange, normed = 'True')
                    histD4 = np.histogram(d4, bins=nBins, range= dRange, normed = 'True')
                    histD5 = np.histogram(d5, bins=nBins, range= dRange, normed = 'True')
                            
                    histTheta1 = np.histogram(theta1, bins=15, range= thetaRange, normed = 'True')
                    
                    mBins = len(histTheta1[0])
                    
                    histTheta2 = np.histogram(theta2, bins=mBins, range= thetaRange, normed = 'True')
                    histTheta3 = np.histogram(theta3, bins=mBins, range= thetaRange, normed = 'True')
                    histTheta4 = np.histogram(theta4, bins=mBins, range= thetaRange, normed = 'True')
                    histTheta5 = np.histogram(theta5, bins=mBins, range= thetaRange, normed = 'True')
                    
                    instance_d1 = np.hstack([histD1[0], histD2[0], histD3[0], histD4[0], histD5[0],  \
                    histTheta1[0], histTheta2[0], histTheta3[0], histTheta4[0], histTheta5[0]])
    
                    
            rad_d1 = np.vstack([rad_d1,instance_d1])
            #print(str(trainData))
            trainData.close()
            
            ## Creates the file for saving the histogram
        return(rad_d1);
        

### HOD representation
def HJPD(filePath):
    rootDir = os.path.dirname(__file__) + '/dataset/' + filePath
    
    # Starting index for arrays. Each index is a frame (ie d1[1] = d1 for frame 1)

    deltaFrame=[]
    hjpd_d1 = [0]*100
    dRange = (0, 1)
    # loops through each file in the /dataset/ directory, and reads the data from each line.
    
    for subdir, dirs, files in os.walk(rootDir):
        for file in files:
            trainData = open(os.path.join(subdir, file), "r")       
            
            for newLine in trainData:
                data = newLine.split()
                data = [float(i) for i in data]
            
            # Checks the values of the first column in each line, and matches them 
            # to the specific joints, with x, y, and z position 
    
                if data[1] == 1:
                    hipCenter_x = data[2]
                    hipCenter_y = data[3]
                    hipCenter_z = data[4]
                    
                elif data[1] == 2:
                    spine_x = data[2]
                    spine_y = data[3]
                    spine_z = data[4]
                    
                elif data[1] == 3:
                    shoulderCenter_x = data[2]
                    shoulderCenter_y = data[3]
                    shoulderCenter_z = data[4]
                    
                elif data[1] == 4:
                    head_x = data[2]
                    head_y = data[3]
                    head_z = data[4]
                    
                elif data[1] == 5:
                    shoulderLeft_x = data[2]
                    shoulderLeft_y = data[3]
                    shoulderLeft_z = data[4]
                
                elif data[1] == 6:
                    elbowLeft_x = data[2]
                    elbowLeft_y = data[3]
                    elbowLeft_z = data[4]
                
                elif data[1] == 7:
                    wristLeft_x = data[2]
                    wristLeft_y = data[3]
                    wristLeft_z = data[4]
                    
                elif data[1] == 8:
                    handLeft_x = data[2]
                    handLeft_y = data[3]
                    handLeft_z = data[4]
                    
                elif data[1] == 9:
                    shoulderRight_x = data[2]
                    shoulderRight_y = data[3]
                    shoulderRight_z = data[4]
                    
                elif data[1] == 10:
                    elbowRight_x = data[2]
                    elbowRight_y = data[3]
                    elbowRight_z = data[4]
                
                elif data[1] == 11:
                    wristRight_x = data[2]
                    wristRight_y = data[3]
                    wristRight_z = data[4]
                    
                elif data[1] == 12:
                    handRight_x = data[2]
                    handRight_y = data[3]
                    handRight_z = data[4]
                    
                elif data[1] == 13:
                    hipLeft_x = data[2]
                    hipLeft_y = data[3]
                    hipLeft_z = data[4]
                    
                elif data[1] == 14:
                    kneeLeft_x = data[2]
                    kneeLeft_y = data[3]
                    kneeLeft_z = data[4]
                    
                elif data[1] == 15:
                    ankleLeft_x = data[2]
                    ankleLeft_y = data[3]
                    ankleLeft_z = data[4]
                
                elif data[1] == 16:
                    footLeft_x = data[2]
                    footLeft_y = data[3]
                    footLeft_z = data[4]
                    
                elif data[1] == 17:
                    hipRight_x = data[2]
                    hipRight_y = data[3]
                    hipRight_z = data[4]
                    
                elif data[1] == 18:
                    kneeRight_x = data[2]
                    kneeRight_y = data[3]
                    kneeRight_z = data[4]
                    
                elif data[1] == 19:
                    ankleRight_x = data[2]
                    ankleRight_y = data[3]
                    ankleRight_z = data[4]
                
                elif data[1] == 20:
                    footRight_x = data[2]
                    footRight_y = data[3]
                    footRight_z = data[4]
                
                    # Stores all of the deltas at each frame
                
                    delta1 = (hipCenter_x - spine_x, hipCenter_y - spine_y, hipCenter_z - spine_z)
                    delta2 = (hipCenter_x - shoulderCenter_x, hipCenter_y - shoulderCenter_y, hipCenter_z - shoulderCenter_z)
                    delta3 = (hipCenter_x - head_x, hipCenter_y - head_y, hipCenter_z - head_z)
                    delta4 = (hipCenter_x - shoulderLeft_x, hipCenter_y - shoulderLeft_y, hipCenter_z - shoulderLeft_z)
                    delta5 = (hipCenter_x - elbowLeft_x, hipCenter_y - elbowLeft_y, hipCenter_z - elbowLeft_z)
                    delta6 = (hipCenter_x - wristLeft_x, hipCenter_y - wristLeft_y, hipCenter_z - wristLeft_z)
                    delta7 = (hipCenter_x - handLeft_x, hipCenter_y - handLeft_y, hipCenter_z - handLeft_z)
                    delta8 = (hipCenter_x - shoulderRight_x, hipCenter_y - shoulderRight_y, hipCenter_z - shoulderRight_z)
                    delta9 = (hipCenter_x - elbowRight_x, hipCenter_y - elbowRight_y, hipCenter_z - elbowRight_z)
                    delta10 = (hipCenter_x - wristRight_x, hipCenter_y - wristRight_y, hipCenter_z - wristRight_z)
                    delta11 = (hipCenter_x - handRight_x, hipCenter_y - handRight_y, hipCenter_z - handRight_z)
                    delta12 = (hipCenter_x - hipLeft_x, hipCenter_y - hipLeft_y, hipCenter_z - hipLeft_z)
                    delta13 = (hipCenter_x - kneeLeft_x, hipCenter_y - kneeLeft_y, hipCenter_z - kneeLeft_z)
                    delta14 = (hipCenter_x - ankleLeft_x, hipCenter_y - ankleLeft_y, hipCenter_z - ankleLeft_z)
                    delta15 = (hipCenter_x - footLeft_x, hipCenter_y - footLeft_y, hipCenter_z - footLeft_z)
                    delta16 = (hipCenter_x - hipRight_x, hipCenter_y - hipRight_y, hipCenter_z - hipRight_z)
                    delta17 = (hipCenter_x - kneeRight_x, hipCenter_y - kneeRight_y, hipCenter_z - kneeRight_z)
                    delta18 = (hipCenter_x - ankleRight_x, hipCenter_y - ankleRight_y, hipCenter_z - ankleRight_z)
                    delta19 = (hipCenter_x - footRight_x, hipCenter_y - footRight_y, hipCenter_z - footRight_z)
                    
                    
                    # Stores the delta at each frame in a large list
                    
                    deltaFrame.append((delta1,delta2,delta3,delta4,delta5,delta6,delta7,delta8,\
                              delta9,delta10,delta11,delta12,delta13,delta14,delta15,delta16,delta17,delta18,delta19))
                    
            instance_hjpd_d1 = np.histogram(deltaFrame, bins=100, range= dRange, normed = 'True')
                    
            hjpd_d1 = np.vstack([hjpd_d1,instance_hjpd_d1[0]])
                        
            trainData.close()
        
        ## Histogram for HJPD
        
        return(hjpd_d1);
        
def convertToSVM(convertFile, filePath):
    
        convertRootDir = os.path.dirname(__file__)  
        rootDir = os.path.dirname(__file__) + '/dataset/' + filePath
        
        dataFile = open(os.path.join(convertRootDir, convertFile), "r")

        act = -2
        label = 1
        activity = ();
        
        for subdir, dirs, files in os.walk(rootDir):
            for file in files:
                #fileName = open(os.path.join(subdir, file), "r")
                actNum = (str(file[1:3]),)
                activity = activity + actNum
                label += 1
        svmLine = str(activity[0]) + '   '
        
        for newLine in dataFile:
            
            data = newLine.split()
            data = [float(i) for i in data]

            act += 1
            for index in range(len(data)):
                
                svmLine = svmLine + str(index) + ':' + str(data[index]) + ' '
            svmLine = svmLine + '   ' +  '\n' +  str(activity[act]) + '    '
        
        return(svmLine);
    
        
### Function calls for test and training functions
            
# RAD Training function

radTrain = RAD('train')
np.savetxt("rad_d1", radTrain, fmt='%f')

## RAD Testing function

radTest = RAD('test')
np.savetxt("rad_d1.t", radTest, fmt='%1.4f')


### HJPD test and train functions
hjpdTrain = HJPD('train')
np.savetxt("hjpd_d1", hjpdTrain, fmt='%f')

hjpdTest = HJPD('test')
np.savetxt("hjpd_d1.t", hjpdTest, fmt='%f')

###

svmRADTest = convertToSVM('rad_d1.t','test')

svmRADFileTest = open('svm_rad_d1.t', 'w')
svmRADFileTest.write(svmRADTest)
svmRADFileTest.close()

###
svmRADTrain = convertToSVM('rad_d1', 'train')

svmRADFileTrain = open('svm_rad_d1', 'w')
svmRADFileTrain.write(svmRADTrain)
svmRADFileTrain.close()
#

###

svmHJPDtest = convertToSVM('HJPD_d1.t', 'test')

svmHJPDFileTest = open('svm_HJPD_d1.t', 'w')
svmHJPDFileTest.write(svmHJPDtest)
svmHJPDFileTest.close()

###
svmHJPDtrain = convertToSVM('HJPD_d1', 'train')

svmHJPDFileTrain = open('svm_HJPD_d1', 'w')
svmHJPDFileTrain.write(svmHJPDtrain)
svmHJPDFileTrain.close()
        

        
