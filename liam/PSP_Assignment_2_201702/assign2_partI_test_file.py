#
#  PSP Assignment 2 (Part I) - Test File
#  Study Period 2, 2017
#
#  DO NOT MODIFY THIS FILE!
#

import list_function

print("\nStart Testing!")

str_list1 = ['r', 'i', 'n', 'g', 'i', 'n', 'g']
str_list2 = ['r', 'e', 'd']
empty = []

print("\nlength Test")
print("List length:", list_function.length(str_list1))
print("List length:", list_function.length(empty))

print("\nto_string Test")
string = list_function.to_string(str_list1)
print("List is:", string)
string = list_function.to_string(str_list1, sep='-')
print("List is:", string)
print("List is:", list_function.to_string(empty))

print("\ncount Test")
print(list_function.count(str_list1, 'i'))
print(list_function.count(str_list2, 'a'))
print(list_function.count(empty, 'z'))

print("\nfind Test")
print(list_function.find(str_list1, 'g'))
print(list_function.find(str_list1, 'z'))

print("\ninsert_value Test")
str_list3 = ['one','three','four', 'five', 'six']
new_list = list_function.insert_value(str_list3, 'two', 1)
print(new_list)
str_list4 = ['i', 't']
str_list4 = list_function.insert_value(str_list4, 'p', 0)
print(str_list4)
str_list4 = list_function.insert_value(str_list4, 's', -1)
print(str_list4)
str_list4 = list_function.insert_value(str_list4, 's', 7)
print(str_list4)

print("\nremove_value Test")
str_list5 = ['r','i','n','g']
new_list = list_function.remove_value(str_list5, 2)
print(new_list)
new_list = list_function.remove_value(str_list5, -1)
print(new_list)
new_list = list_function.remove_value(str_list5, 10)
print(new_list)


print("\n----------")


num_list1 = [1, 7, 2, 3, 7, 7]

print("\nlength Test")
print("List length:", list_function.length(num_list1))

print("\nto_string Test")
print('List is:', list_function.to_string(num_list1))
print('List is:', list_function.to_string(num_list1, sep=' - '))

print("\ncount Test")
print(list_function.count(num_list1, 7))

print("\nfind Test")
print(list_function.find(num_list1, 7))

print("\ninsert_value Test")
num_list2 = [1, 3, 4, 5, 6]
num_list2 = list_function.insert_value(num_list2, 2, 1)
print(num_list2)

print("\nremove_value Test")
num_list3 = [1, 3, 4, 5, 6]
num_list3 = list_function.remove_value(num_list3, 1)
print(num_list3)

print("\nEnd Testing!\n")


