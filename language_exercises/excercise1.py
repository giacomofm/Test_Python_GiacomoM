# 1. Write a function `dict_values_ascending` that accecpts a dictionary as an argument and returns a list of dictionary *values* in ascending order

dic = {'mike': 'room 3', 'giulio': 'desk 2', 'marco': 'desk 1'}

def dict_values_ascending(dictionary):
	values_list=[]
	for value in dictionary:
		values_list.append(dictionary[value])
	values_list.sort()
	print values_list

dict_values_ascending(dic)