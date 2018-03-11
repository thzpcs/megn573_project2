### RAD/HJPD representation for Skeletal tracking

Written by Skyler Morris for MEGN 573 at the Colorado School of Mines

The objective is to implement the RAD representation to convert
all data instances in the folder Train into a single training
file rad d1, each line corresponding the RAD representation
of a data instance. Similarly, all instances in the folder Test
needs to be converted into a single testing file rad d1.t

This project also implements HJPD in a similar fashion, creating a 
histogram for each training instance, and then concatenating all of the
histograms into a single array, and saving it to the HJPD testing and 
training files

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

## Running

All that is needed to run this script are all of the files contained within the T1_Skyler_Morris.tar archive
extracted into the directory of your choosing. 

Once extracted, open up a Python shell, navigate to the directory, and run the 
RAD_Star_Skeleton.py file. All 4 RAD/HJPD training/testing files will be generated in the directory.

## Built With

* [Anaconda 3.6.3](https://anaconda.org/anaconda/python)- Python framework used
* [Spyder] - IDE used, comes with Anaconda 3.6.3
* [Windows 10/Ubuntu 16.4] - Operating systems used for development


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

Git was used for versioning For the versions available, see https://github.com/thzpcs/megn573_project2

## Authors

* **Skyler Morris** - *Initial work* - [PurpleBooth](https://github.com/thzpcs)

## License

This project is licensed under the MIT License 

## Acknowledgments

* Thank you to Dr. Hao Zhang for assisance and inspiration for this assignment