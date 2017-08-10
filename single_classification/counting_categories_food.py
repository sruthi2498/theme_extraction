from __future__ import division
import os
import random
import re

fpath=os.path.join("data", "food_data_set.txt")
f=open(fpath,'r')

categories=[]
i=0

for row in f:
	i=i+1
	row=row.rstrip()
	row=row.split('"')
	if(len(row)==9):
		rest=row[1]
		cuisine=row[3]
		rev=row[5]
		cat=cuisine
		if(cat not in categories):
			
			categories.append(cat)

print i			
List={}
for cat in categories:
	a=[]
	List[cat]=a

print categories

fpath=os.path.join("data", "food_data_set.txt")
f=open(fpath,'r')
for row in f:
	row=row.rstrip()
	row=row.split('"')
	if(len(row)==9):
		rest=row[1]
		cuisine=row[3]
		rev=row[5]
		cat=cuisine
		List[cat].append(rev)

for key,val in List.iteritems():
	print key,":",len(val)

f.close()