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


def CreateDataSet(file1):
	data=[]
	categories=[]
	target=[]
	categories=['taste', 'decor', 'atmosphere', 'company', 'filler', 'tax', 'food', 'reservation', 'opening time', 'price', 'location', 'quantity', 'delivery', 'rating', 'seating', 'waiters', 'service', 'menu', 'waiting time', 'sanitation', 'bar', 'presentation']
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
				target.append(categories.index(t))
			#print row


	target_names=categories
	freq=Counter(target)


	#print freq
	
	return data,target_names,target

	#print "target_names / categories : ",target_names

def CreateTargetNames():
	categories=['taste', 'decor', 'atmosphere', 'company', 'filler', 'tax', 'food', 'reservation', 'opening time', 'price', 'location', 'quantity', 'delivery', 'rating', 'seating', 'waiters', 'service', 'menu', 'waiting time', 'sanitation', 'bar', 'presentation']
	return categories
def CreateTrainingDataSet(file1):
	data=[]
	categories=[]
	target=[]
	categories=['taste', 'decor', 'atmosphere', 'company', 'filler', 'tax', 'food', 'reservation', 'opening time', 'price', 'location', 'quantity', 'delivery', 'rating', 'seating', 'waiters', 'service', 'menu', 'waiting time', 'sanitation', 'bar', 'presentation']
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
				target.append(categories.index(t))
			#print row


	target_names=categories
	freq=Counter(target)


	#print freq
	
	return data,target

	#print "target_names / categories : ",target_names

def CreateTestingDataSet(file1):
	data=[]
	categories=[]
	target=[]
	categories=['taste', 'decor', 'atmosphere', 'company', 'filler', 'tax', 'food', 'reservation', 'opening time', 'price', 'location', 'quantity', 'delivery', 'rating', 'seating', 'waiters', 'service', 'menu', 'waiting time', 'sanitation', 'bar', 'presentation']
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
				target.append(categories.index(t))
			#print row


	target_names=categories
	freq=Counter(target)


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
	train=data[:947]
	target_train=target[:947]
	test=data[947:]
	target_test=target[947:]
	return train,target_train,test,target_test

def TrainDataSetNVB(train,target_train):
	
	text_clf = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', MultinomialNB())])
	text_clf = text_clf.fit(train, target_train)

	#docs_test_2 = test
	#predicted_2 = text_clf.predict(docs_test_2)

	return text_clf


def TrainDataSetSGD(train,target_train):
	
	text_clf =  Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, n_iter=5, random_state=42))])
	text_clf = text_clf.fit(train, target_train)

	#docs_test_2 = test
	#predicted_2 = text_clf.predict(docs_test_2)

	return text_clf


def Predict(test,text_clf):
	predicted = text_clf.predict(test)
	return predicted

def TestAccuracy(target_test,predicted):
	print (np.mean(predicted== target_test))


def CategorizeSingleReview(new_review,text_clf,target_names):
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
	actual_op=[]

	for doc, category in zip(new_review, predicted):
		each_sent={}
		each_sent['sent']=doc
		each_sent['cat']=target_names[category]
		actual_op.append(each_sent)

	#print actual_op
	frequencies_rev = Counter(predicted)
	return frequencies_rev, actual_op
	#print "here"
	#return predicted,new_review

def CalculateResult(frequencies_rev,target_names):
	total=frequencies_rev[0]+frequencies_rev[1]+frequencies_rev[2]+frequencies_rev[3]+frequencies_rev[4]
	'''print "This review talks about : "
	print target_names[0],(frequencies_rev[0]/total)*100,"%"
	print target_names[1],(frequencies_rev[1]/total)*100,"%"
	print target_names[2],(frequencies_rev[2]/total)*100,"%"
	print target_names[3],(frequencies_rev[3]/total)*100,"%"
	print "\n"'''
	#print str((frequencies_rev[0]/total))
	#st="This review talks about : "+ target_names[0]+str((frequencies_rev[0]/total)*100)+"% "+target_names[1]+str((frequencies_rev[1]/total)*100)+"% "+target_names[2]+str((frequencies_rev[2]/total)*100)+"% "+target_names[3]+str((frequencies_rev[3]/total)*100)+"% "
	st= [(frequencies_rev[0]/total)*100,(frequencies_rev[1]/total)*100,(frequencies_rev[2]/total)*100,(frequencies_rev[3]/total)*100,(frequencies_rev[4]/total)*100]
	return st