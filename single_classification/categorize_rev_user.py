from __future__ import division
import os
import categorize_rev
from categorize_rev import *
from categorize_food_rev import *
import pandas
'''
fpath=os.path.join("data", "categorized_reviews.txt")
f=open(fpath,'r')'''

fpath3=os.path.join("data", "food_data_set.txt")
f3=open(fpath3,'r')

fdata,ftarget_names,ftarget=CreateDataSetFood(f3)
print "fdata",len(fdata)
ftarget_name=CreateTargetNamesFood()

ftrain,ftarget_train=CreateTestAndTrainDataSetsFood(fdata,ftarget)


ftext_clf_NVB=TrainDataSetNVBFood(ftrain,ftarget_train)

ftext_clf_SGD=TrainDataSetSGDFood(ftrain,ftarget_train)
'''
fpredict_NVB=PredictFood(ftest,ftext_clf_NVB)

fpredict_SGD=PredictFood(ftest,ftext_clf_SGD)

print "Accuracy Naive Bayes Food"
TestAccuracyFood(ftarget_test,fpredict_NVB)

print "Accuracy Support Vector Machine Food"
TestAccuracyFood(ftarget_test,fpredict_SGD)'''
###########################################################################################################
fpath2=os.path.join("data", "training_data_set.txt")
f2=open(fpath2,'r')
fpath3=os.path.join("data", "testing_data_set_200.txt")
f3=open(fpath3,'r')
train,target_train=CreateTrainingDataSet(f2)
test,target_test=CreateTestingDataSet(f3)
target_names=CreateTargetNames()

text_clf_NVB=TrainDataSetNVB(train,target_train)

text_clf_SGD=TrainDataSetSGD(train,target_train)

predict_NVB=Predict(test,text_clf_NVB)

predict_SGD=Predict(test,text_clf_SGD)

print "Accuracy Naive Bayes"
TestAccuracy(target_test,predict_NVB)

print "Accuracy Support Vector Machine"
TestAccuracy(target_test,predict_SGD)
n=len(test)

for i in range(0,n):
	print i
	rev=test[i]
	freq,actual_op=CategorizeSingleReview(rev,text_clf_SGD,target_names)
	if(actual_op[0]['cat']!=target_names[target_test[i]]):
		print actual_op[0]['sent']
		print "category : ", actual_op[0]['cat'],", actual : ",target_names[target_test[i]]
	
	'''
	if(actual_op[0]['cat']=='food'):
		print "-----"
		ffreq,factual_op=CategorizeSingleReviewFood(rev,ftext_clf_SGD,ftarget_names)
		print "food category : ",factual_op[0]['cat'],", actual : ",ftarget_names[ftarget_test[i]]
		
		print "-----"
	'''

'''

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
'''
