from __future__ import division
import os
import random
import re

fpath=os.path.join("data", "original_data_set.txt")
f=open(fpath,'r')

sentenceEnders = re.compile('[.!?]')

All_reviews=[]
for row in f:
	row=row.rstrip()
	row=row.split('"')
	if(len(row)==7):
		rest=row[1]
		cuisine=row[3]
		rev=row[5]
		sentenceList = sentenceEnders.split(rev)
		rev=sentenceList
		for r in rev:
			if(len(r)>=5):
				#print r
				x="\""+rest+"\",\""+cuisine+"\",\""+r+"\""
				#print x
				All_reviews.append(x)
				#f2.write(("\""+rest+"\",\""+cuisine+"\",\""+r+"\"\n"))
		

print "all"
print All_reviews[0]
random.shuffle(All_reviews)
print All_reviews[0]

f.close()

Train=[]
Test=[]
n=len(All_reviews)
for i in range(0,1000):
	Train.append(All_reviews[i])
for i in range(1000,n):
	Test.append(All_reviews[i])

print len(Test)

fpath=os.path.join("data", "training_data_set.txt")
f=open(fpath,'a+')
for rev in Train:
	f.write(rev)
	f.write('\n')

f.close()

fpath=os.path.join("data", "testing_data_set.txt")
f=open(fpath,'a+')
for rev in Test:
	f.write(rev)
	f.write('\n')

f.close()



