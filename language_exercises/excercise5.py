# coding: utf-8
# 5. write a python module `esercizio5.py` that reads the remote HTTP endpoint http://ialpython.apiary.io/laboratories 
# 	and prints to standard output all the laboratories with network status `down`

import requests

resp = requests.get('http://ialpython.apiary.io/laboratories')
laboratories = resp.json() #ne risulta una lista di dizionari

laboratorie=[]

for dictionary in laboratories:
	for word in dictionary:
		if word=="network_status":
			if dictionary[word]=="down":
				laboratorie.append(dictionary["name"])

print laboratorie