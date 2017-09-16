# File : fileName.py
# Author : your name
# Saibt Id : your saibt id
# Description : Assignment 2   place assignment description here . . .
# This is my own work as defined by the University ’s
# Academic Misconduct pol icy .



# Function length() - get the length of given list, return the length
def length(my_list):
	counter = 0
	for i in my_list:
		counter += 1
	return counter


# Function to_string() - parse list to string, return a string
def to_string(my_list, sep=', '):
	if length(my_list) == 0:
		return ""
	output = ""
	for i in range(length(my_list)-1):
		output = output + str(my_list[i]) + sep
	output = output + str(my_list[length(my_list)-1])
	return output
		

# Function count() - count the occurence of specified char in list
def count(my_list, value):
	counter = 0
	for item in my_list:
		if item == value:
			counter +=1
	return counter


# Function find() - find the value in the list , return index of the value
def find(my_list, value):
	for index in range(length(my_list)):
		if my_list[index] == value:
			return index
	return -1
	

# Function insert_value() - insert a value into list, return a new list
def insert_value(my_list, value, insert_position):
	lst_length = length(my_list)
	# if insert position less than 0
	if insert_position <=0:
		return [value] + my_list
	# if insert position greater than the length 
	if insert_position >= lst_length:
		return my_list + [value]
	array = []
	for i in range(0, insert_position):
		array.append(my_list[i])
	array.append(value)
	for i in range(insert_position, lst_length):
		array.append(my_list[i])
	return array

# Function remove_value() - remove a value in the specified index, return the new list
def remove_value(my_list, remove_position):
	lst_length = length(my_list)
	result = []
	# if remvoe position less than 0
	if remove_position <= 0:
		for i in range(1, lst_length):
			result.append(my_list[i])
		return result
	# if remove position great than length
	if remove_position >= lst_length:
		for i in range(0, lst_length-1):
			result.append(my_list[i])
		return result
	
	for i in range(0, remove_position):
		result.append(my_list[i])
	for i in range(remove_position+1, lst_length):
		result.append(my_list[i])
	return result




