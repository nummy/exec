import sys
import re
from collections import defaultdict
from itertools import combinations,chain

def open_file():
    # open file and return file pointer
    fp = None
    filename = input("Filename:")
    try:
        fp = open(filename,'r')
    except:
    	print("file does not exits")
    	sys.exit()
    return fp


def read_file(fp):
	"""
	read file
	"""
	data = fp.read().strip()
	arr = re.split(r"\s+", data)
	values = []
	for item in arr:
		if not item.isdigit():
			print("Sorry, input file does not store valid data")
			sys.exit()
		values.append(int(item))
	if len(values) < 2:
		print("At least two positive integers")
		sys.exit()
	for value in values:
		if value <= 0:
			print("Sorry, input file does not store valid data")
			sys.exit()
	return values


def can_make_up(data):
	"""
	whether or not this structure makes up for a perfect ride
	"""
	length = len(data)
	start = data[0]
	end = data[-1]
	step = (end-start)//(length-1)
	if step == 0:
		step = 1
	if data == list(range(start, end+step,step)):
		return True
	else:
		return False

def get_longest_ride(data):
	"""
	get the length of the longest good ride
	"""
	length = len(data)
	start = 0
	second = 1
	step = data[second] - data[start]
	res = {0:1}
	for i in range(2, length):
		if (data[i]-data[second]) == step:
			res[start] =  res.get(start,1) + 1
			second = i
		else:
			start = i-1
			second = i
			step = data[second]-data[start]
			res[start] = 1
	sorted_res = sorted(res.items(), key=lambda data:data[1], reverse=True)
	start = sorted_res[0][0]
	count = sorted_res[0][1]
	return start, count, data[start:count+start+1]

def remove(list1,start,count):
	"""
	get remain structure
	"""
	res = []
	for index, elem in enumerate(list1):
		if index<=start or index > start+count:
			res.append(elem)
	return res


def get_equid(arr):
	"""
	get all combinations
	"""
	length = len(arr)
	if length <= 2:
		return arr
	res = []
	for i in range(length+1,2,-1):
		temp = combinations(arr,i)
		for item in temp:
			if can_make_up(item):
				return item
	return []



def main():
	"""
	main function
	"""
	#fp = open_file()
	fp = open("data.txt", "r")
	structure = read_file(fp)
	print("The structure is :%s" % structure)
	print("Can this structure makes up a perfect ride? :%s" % "Yes" if can_make_up(structure) else "No")
	start, count , longest = get_longest_ride(structure)
	print("The length of the longest good ride is : %s"%count)
	print("The good ride is : %s" % longest)
	remain_structure = remove(structure, start,count)
	if len(remain_structure) < 2:
		print("How many pillars to remove to build a perfect ride from the remaining ones? : 0")
		sys.exit()
	print("Remain structure : %s"%remain_structure)
	equid = get_equid(structure)
	length_remain = len(structure)
	length_final = len(equid)
	print("How many pillars to remove to build a perfect ride from the remaining ones? : %s" % (length_remain-length_final))
	removes = [item for item in structure if item not in equid]
	print("Final good ride: %s" % equid)
	print("Removed pillars: %s" % removes)


if __name__ == "__main__":
	main()

