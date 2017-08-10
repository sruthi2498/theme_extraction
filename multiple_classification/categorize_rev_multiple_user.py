from __future__ import division
import os
from categorize_rev_multiple import *

fpath1=os.path.join("data", "training_data_set.txt")
f1=open(fpath1,'r')

fpath2=os.path.join("data", "testing_data_set_200.txt")
f2=open(fpath2,'r')

target_names=CreateTargetNames()

train,target_train=CreateTrainingDataSet(f1)
test,target_test=CreateTestingDataSet(f2)

train=np.array(train)
test=np.array(test)
mlb,MLBtarget_train=CreateMLBForTargetTrain(target_train)
mlb2,MLBtarget_test=CreateMLBForTargetTrain(target_test)
classf=TrainDataSetMultiple(train,MLBtarget_train)

predicted=Predict(test,classf)

print "test:"
CategorizeTest(test,classf,target_names,mlb)
print test[0]
print predicted[0]
print MLBtarget_train[0]
print TestAccuracy(MLBtarget_test[0],predicted[0])
'''
n=len(predicted)
m=0
for i in range(0,len(predicted)):
	each_accur=TestAccuracy(MLBtarget_test[i],predicted[i])
	print each_accur
	m=m+each_accur
print "total accuracy:",m/n
	
test2=[" Would definitely like to go again and try other items on the menu"," Before I forget, the staff here is very courteous and prompt too"," Both were quite good"," The drinks are served in mason jars which I thought was perfectly in sync with the theme of the place"," Also you can give your mobile to them to play your own playlist"]
CategorizeTest(test2,classf,target_names,mlb)'''