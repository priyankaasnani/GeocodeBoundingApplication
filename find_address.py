import csv
import sys

#This function accepts filename and area coordinate argumets from command line 
#and returns addresses which belong to that coordinate
def getAddress(param):
	filename = param[1]
	coordinate = param[2]
	addresses = []
	try:
		with open(filename, 'rb') as fcontent:
			data = csv.reader(fcontent, delimiter= " ")
			coordinates = next(data)
			if coordinate in coordinates:
				mapping_index = coordinates.index(coordinate)
			for row in data:
				addresses.append(row[mapping_index])
			return addresses
	except IOError:
		print "The file does not exist"

address = getAddress(sys.argv)
for address_list in address:
	print address_list
