README FILE

------------------------------------------------------------------------------------------------------------
Project Title
------------------------------------------------------------------------------------------------------------
Geocode and Bounding
	->Here we read in the text file which contains coorrdinates of a particular area and their corresponding addresses 
	->The first line of the file will be the coordinates of a particular area and the subsequent lines will be 
	address
	->A single space is used as a delimeter in mapped_coordinates.txt file i.e., " "
	->The program outputs all the addressess that are inside the particular coordinate
	->The program is built using Python 2.7

----------------------------------------------------------------------------------------------------------------
Prerequisites
----------------------------------------------------------------------------------------------------------------
We need to have csv and sys module installed. These modules are already included in the package list when we
install Python. So we don't need to install them sepratly

---------------------------------------------------------------------------------------------------------------
Setting the Environment
---------------------------------------------------------------------------------------------------------------
->We need to have Python 2.7 installed
->Run find_address.py on command line:
	Example: python find_address.py mapped_coordinates.txt '(37.5,-122.5)'
-> Output Example: 1706 Forest View Ave Hillsborough CA 94010
					1 Hacker Way, Menlo Park, CA
					3045 Novato Blvd, Novato, CA 94947
					45 South Cross Lane Encino, CA 91316

---------------------------------------------------------------------------------------------------------------
Running the tests
---------------------------------------------------------------------------------------------------------------
->We use pytest module to run automated tests
->Run following commands on the root of the folder
	pip install pytest
	python -m pytest