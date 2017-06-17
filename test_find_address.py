import sys
sys.argv = ['find_address.py', 'mapped_coordinates.txt', '(37.5,-122.5)']
import find_address

def testAddress():
	assert find_address.getAddress(sys.argv) == ['1706 Forest View Ave Hillsborough CA 94010', '1 Hacker Way, Menlo Park, CA',
													'3045 Novato Blvd, Novato, CA 94947', '45 South Cross Lane Encino, CA 91316']