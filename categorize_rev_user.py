from __future__ import division
import os
import categorize_rev
from categorize_rev import *
import pandas

fpath=os.path.join("data", "categorized_reviews.txt")
f=open(fpath,'r')
fpath2=os.path.join("data", "categorized_reviews_sentences_2.txt")

f2=open(fpath2,'a+')
f2=open(fpath2,'r')

data,target_names,target=CreateDataSet(f2)
print len(data)
print target_names

train,target_train,test,target_test=CreateTestAndTrainDataSets(data,target)

text_clf_NVB=TrainDataSetNVB(train,target_train)

text_clf_SGD=TrainDataSetSGD(train,target_train)

predict_NVB=Predict(test,text_clf_NVB)

predict_SGD=Predict(test,text_clf_SGD)

print "Accuracy Naive Bayes"
TestAccuracy(target_test,predict_NVB)

print "Accuracy Support Vector Machine"
TestAccuracy(target_test,predict_SGD)

fpath2=os.path.join("data", "op_freq.txt")
f2=open(fpath2,'w').close()
f2=open(fpath2,'a+')
fpath3=os.path.join("data", "op.txt")
f3=open(fpath3,'w').close()
f3=open(fpath3,'a+')

for row in f:
	#print row
	row=row.rstrip()
	row=row.split('"')
	if(len(row)==7):
		rest=row[1]
		cuisine=row[3]
		rev=row[5]
		#print rev
		freq,actual_op=CategorizeSingleReview(rev,text_clf_SGD,target_names)
		s=CalculateResult(freq,target_names)
		#print type(s)
		f2.write(str(s[0])+","+str(s[1])+","+str(s[2])+","+str(s[3])+"\n")
		print len(actual_op)
		for elem in actual_op:
			print elem
			f3.write(elem[0]+"/")

		f3.write("\n")

f.close()
f2.close()
f3.close()

