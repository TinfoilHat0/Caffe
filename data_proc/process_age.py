#!/usr/bin/python

import os, sys
ages = {}
	        
#1. go over images, label them using genders dict. and create a new labels.txt
resultsPath ="/home/comp/caffe-master/data/gender_data/images"
dataPath = "/home/comp/caffe-master/data/gender_data/images"
cnt = 0
dirs = os.listdir( dataPath )
f = open('trainAge.txt','w')
for file in dirs:
   parsed = file.split("_")
   age = parsed[0]
   f.write( resultsPath + '/'+ file + ' ' + str(age) + '\n')
   cnt += 1
   if cnt > 1999:#using only 2k images, decrement/increment as you please
	break
   

f.close()
	
   
