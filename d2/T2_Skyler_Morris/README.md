### RAD/HJPD representation for Skeletal tracking

Written by Skyler Morris for MEGN 573 at the Colorado School of Mines


Converts the training and testing files (i.e., the outputs
of the code to build the representations in Deliverable
1 to a format that can be used by LIBSVM.

Apply LIBSVM to learn a C-SVM model with the RBF
kernel from the training data, and use the learned model
to predict behavior labels of the testing data, which
will generate a result file, e.g., rad d2.t.predict,
and cust d2.t.predict.

Evaluate its performance based upon the output results
using the performance metrics of accuracy and confusion
matrix.

# Implementation Notes

For the RAD tracking, only the external joints are used, with hipCenter used as the centroid for calculation.
These joints include hipCenter, head, handLeft, handRight, footLeft, footRight
Please see the code and comments for further details
The histogram utilizes an automatically calculated number of bins based on the ideal number
as calculated within the histogram function. See code for further details

For HJPD representation, all 20 joints are utilized, and a similar method for the number of bins used
is shown in the code.

## Prerequisites

You will need Python 3.6, and an operating system capable of running Python 3.6 such as Ubuntu 16.4 or Windows 10
You will also need the numpy and os libraries, which are standard within Python 3.6.3

You will need the RAD_Star_Skeleton script, which is included in the package, and is used to generate the testing and training
files

libsvm-3.22 is included in the package, and must be installed according to the READMEs within

## Running

All that is needed to run this script are all of the files contained within the T1_Skyler_Morris.tar archive
extracted into the directory of your choosing. 

Once extracted, open up a Python shell, navigate to the directory, and run the 
RAD_Star_Skeleton.py file. All 4 RAD/HJPD training/testing files will be generated in the directory.

The RAD/HJPD files will also generate svm_* files, which can be used with any svm program.

RAD_Star_Skeleton includes a method to convert any file into an SVM appropriate file format. See documentation for details.


## SVM Notes

All of the model and prediction results can be found in the root directory (*.model, *.predict, the *.bmp/png files, etc)

The ideal C and Gamma values found were somewhat inconsistent, as they did not seem to affect the overall prediction accuracy,
even when using auto scaling features such as with easy.py. Because of this, the prediction accuracy is extremely low, effectively
bordering on useless since the program would only predict a single instance for all of the testing files. 

Hopefully guidance and mercy will be provided by the instructor on this issue, as the author of this code hopes to understand this issue, 
even though it did not meet the assignment guidelines perfectly despite multiple days straight working on the assignment.

Unfortunately, there was insufficient time to investigate this issue, and further testing will have to be performed with the package

The appropriate values and parameters used can be seen at the top lines of the .model files, with the 2 models as follows:

RAD:
svm_type c_svc
kernel_type rbf
gamma 0.0078125
nr_class 6
total_sv 72
rho -0.185952 -4.56173 -0.55241 -1.55185 -0.0309724 -1.83309 -0.319858 -0.499693 -0.273181 2.52996 2.21857 2.42743 0.279968 -0.718783 -2.09015
label 8 12 15 10 16 13
nr_sv 12 12 12 12 12 12
SV
C 512

HJPD:
svm_type c_svc
kernel_type rbf
gamma 8
nr_class 6
total_sv 74
rho -0.0848583 -0.0297535 -0.0493904 -0.0996572 0.00238915 0.0481058 -0.020691 -0.0265176 0.0370859 -0.057304 -0.125014 -0.0262465 -0.00631669 0.0559432 0.0272551
label 8 12 15 10 16 13
nr_sv 13 13 12 12 12 12
SV
C 2


## Built With

* [Anaconda 3.6.3](https://anaconda.org/anaconda/python)- Python framework used
* [Spyder] - IDE used, comes with Anaconda 3.6.3
* [Windows 10/Ubuntu 16.4] - Operating systems used for development
* [LIBSVM 3.22]


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

Git was used for versioning For the versions available, see https://github.com/thzpcs/megn573_project2

## Authors

* **Skyler Morris** - *Initial work* - [thzpcs](https://github.com/thzpcs)

## License

This project is licensed under the MIT License 

## Acknowledgments

* Thank you to Dr. Hao Zhang for assistance and inspiration for this assignment
* Thank you to the LIBSVM team, and their acknowledgments 
