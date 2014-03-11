#2. Write a function named `add_dict(dict_1, dict_2)` that joins the two dictionaries provided as arguments and returns 
#	a single dictionary with all the items of `dict_1` and `dict_2`

dic_1 = {'giulio': 'desk 2', 'marco': 'desk 1', 'mike': 'room 3'}
dic_2 = {'patate': 'patatine', 'cipolle': 'soffritto', 'pomodori': 'passata'}

def add_dict(dict_1, dict_2):
	dict_blue={}
	for word in dict_1:
		dict_blue[word]=dict_1[word]
	for word in dict_2:
		dict_blue[word]=dict_2[word]

	print dict_blue

add_dict(dic_1, dic_2)