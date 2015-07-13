#!/usr/bin/python

import os, sys
#1. open input.txt, store labels in a dict i.e genders[name] = f/m(0/1)
persons = {}
cnt = 1
with open("persons.txt", "r") as ins:
    for line in ins:
	parsed = line.split()
	name = parsed[1].split("_")
	name = name[1] + name[2]
	persons[name] = cnt
	cnt += 1
	        
#2. go over images, label them using dict. and create a new labels.txt
cnt = 0
resultsPath ="/home/comp/caffe-master/data/gender_data/images"
dataPath = "/home/comp/caffe-master/data/gender_data/images"
dirs = os.listdir( dataPath )
f = open('trainPerson.txt','w')
for file in dirs:
   parsed = file.split("_")
   name = parsed[1] + parsed[2]
   g = persons.get(name, "default")
   if g != "default":
	f.write( resultsPath + '/'+ file + ' ' + str(g) + '\n')
	cnt += 1

f.close()
	
   
