#!/usr/bin/python

import os, sys
#1. open input.txt, store labels in a dict i.e genders[name] = f/m(0/1)
genders = {}
with open("labels.txt", "r") as ins:
    for line in ins:
	parsed = line.split()
	name = parsed[1].split("_")
	name = name[1] + name[2]
	gender = 1
	if parsed[3] == "F":
		gender = 0
	genders[name] = gender
	        
#2. go over images, label them using genders dict. and create a new labels.txt
resultsPath ="/home/comp/caffe-master/data/gender_data/images"
dataPath = "/home/comp/gender_data/AlignedSym"

cnt = 0
dirs = os.listdir( dataPath )
f = open('trainGender.txt','w')
for file in dirs:
   parsed = file.split("_")
   name = parsed[1] + parsed[2]
   g = genders.get(name, "default")
   if g != "default":
	f.write( resultsPath + '/'+ file + ' ' + str(g) + '\n')
	cnt += 1
   if cnt > 1999:#using only 2k images, decrement/increment as you please
	break
   

f.close()
	
   
