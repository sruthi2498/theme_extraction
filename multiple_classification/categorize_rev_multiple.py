from __future__ import division
import os
import logging
logging.basicConfig()
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import numpy as np
from collections import Counter
import random
from sklearn.linear_model import SGDClassifier
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics import accuracy_score

def CreateTargetNames():
	categories=['filler', 'taste', 'price', 'tax', 'quantity', 'location', 'food', 'seating', 'atmosphere', 'service', 'waiters', 'company', 'decor', 'rating', 'menu', 'presentation', 'bar', 'waiting time', 'delivery', 'sanitation', 'reservation', 'opening time']

	categories=sorted(categories)
	return categories

def CreateMLBForTargetTrain(target_train):
	mlb = MultiLabelBinarizer()
	MLBtarget_train = mlb.fit_transform(target_train)
	return mlb,MLBtarget_train

def CreateTrainingDataSet(file1):
	data=[]
	target=[]
	rows=[]
	for row in file1:
		rows.append(row)
	

	for row in rows:
		row=row.rstrip()
		row=row.split('"')
		#print len(row)
		if(len(row)<9):
			print row
		if(len(row)==9):
				other=0
				data.append(row[5])
				t=row[7]
				t=t.split(',')
				target.append(t)
			#print row

	return data,target

	#print "target_names / categories : ",target_names

def CreateTestingDataSet(file1):
	data=[]
	target=[]
	rows=[]
	for row in file1:
		rows.append(row)
	
	random.shuffle(rows)
	for row in rows:
		row=row.rstrip()
		row=row.split('"')
		#print len(row)
		if(len(row)<9):
			print row
		if(len(row)==9):
				other=0
				data.append(row[5])
				t=row[7]
				t=t.split(',')
				target.append(t)
			#print row
	data=np.array(data)
	target=np.array(target)

	#print freq
	
	return data,target

	#print "target_names / categories : ",target_names
def CreateTestAndTrainDataSets(data,target):
	'''
	train=data[100:]
	target_train=target[100:]

	test=data[:283]
	target_test=target[:283]

	return train,target_train,test,target_test'''
	train=data[:13]
	target_train=target[:13]
	test=data[13:]
	target_test=target[13:]
	return train,target_train,test,target_test


def TrainDataSetMultiple(train,MLBtarget_train):
	classifier = Pipeline([('vectorizer', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', OneVsRestClassifier(LinearSVC()))])
	classifier.fit(train, MLBtarget_train)
	return classifier

def Predict(test,classifier):
	predicted = classifier.predict(test)
	return predicted

def TestAccuracy(target_test,predicted):
	return accuracy_score(target_test, predicted)


def CategorizeSingleReview(new_review,text_clf,target_names,mlb ):
	#print "using ",text_clf
	new_review=new_review.rstrip()
	new_review=new_review.split('.')
	for rev in new_review:
		#print rev

		if(len(rev)<=5):
			new_review.remove(rev)
		a=rev.split()
		if(len(a)<=1):
			#print a
			if(rev in new_review):
				new_review.remove(rev)
	list_of_predictions=[]
	predicted = text_clf.predict(new_review)
	#print predicted
	all_labels = mlb.inverse_transform(predicted)

	for item, labels in zip(new_review, all_labels):
	    print('{0} => {1}'.format(item, ', '.join(labels)))
'''
	actual_op=[]

	for doc, category in zip(new_review, predicted):
		each_sent={}
		each_sent['sent']=doc
		each_sent['cat']=target_names[category]
		actual_op.append(each_sent)

	#print actual_op
	frequencies_rev = Counter(predicted)
	return frequencies_rev, actual_op'''

def CategorizeTest(test,classifier,target_names,mlb ):
	predicted = classifier.predict(test)
	all_labels = mlb.inverse_transform(predicted)
	blank=0
	double=0
	for item, labels in zip(test, all_labels):
		if(len(labels)==0):
			print "multiple returned blank"
			
		else:
			print('{0} => {1}'.format(item, ', '.join(labels)))
	