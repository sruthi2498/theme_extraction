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


fpath=os.path.join("data", "categorized_reviews.txt")
f=open(fpath,'r')
fpath2=os.path.join("data", "categorized_reviews_sentences_2.txt")

f2=open(fpath2,'a+')
'''
for row in f:
	row=row.rstrip()
	row=row.split('"')
	print len(row)
	if(len(row)==7):
		rest=row[1]
		cuisine=row[3]
		rev=row[5]
		#print rest,type(rest),len(rest)
		#print cuisine,type(cuisine),len(cuisine)
		#print rev,type(rev),len(rev)
		rev=rev.split('.')
		#print rev
		for r in rev:
			if(len(r)>=5):
				f2.write(("\""+rest+"\",\""+cuisine+"\",\""+r+"\"\n"))


f.close()
f2.close()
'''
data=[]
categories=[]
target=[]
f2=open(fpath2,'r')
categories=['food','ambience','price','service']
rows=[]
for row in f2:
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
			if(row[7]!='other' and row[7]!='delivery' and row[7]!='order'):
				data.append(row[5])
				t=row[7]
				target.append(categories.index(t))
		#print row


target_names=categories
'''print target_names
print data
print target'''

print "target_names / categories : ",target_names




#docs_new = ['Keep a look out for the adorable wall-art','They serve the best donuts in the world surely']
docs_new=[]
rest=[]
cuisine=[]
f=open(fpath,'r')
f2=open(fpath2,'a+')
for row in f:
	row=row.rstrip()
	row=row.split('"')
	#print len(row)
	if(len(row)==7):
		
		rest.append(row[1])
		cuisine.append(row[3])
		rev=row[5]
		#print rest,type(rest),len(rest)
		#print cuisine,type(cuisine),len(cuisine)
		#print rev,type(rev),len(rev)
		rev=rev.split('.')
		#print rev
		for r in rev:
			docs_new.append(r)


f.close()

docs_new=[]
docs_new = ['Keep a look out for the adorable wall-art','They serve the best donuts in the world surely']

count_vect = CountVectorizer()
#print count_vect
#print "data",len(data)
frequencies = Counter(target)
#print "target freq ( frequency of each category in the entire sample)",frequencies

train=data[210:]
target_train=target[210:]

#print "train",len(train),"target_train",len(target_train)
#print target_train
frequencies_target_train = Counter(target_train)
#print frequencies_target_train
test=data[:200]
target_test=target[:200]

X_train_counts = count_vect.fit_transform(train)
#print "X_train_counts ",X_train_counts
#print "X_train_counts.shape ",X_train_counts.shape
#print "len(target_train)",len(target_train)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
#print type(X_train_tfidf)
#print "X_train_tfidf.shape ",X_train_tfidf.shape

clf = MultinomialNB().fit(X_train_tfidf, target_train)

X_new_counts = count_vect.transform(docs_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)
i=0
#for doc, category in zip(docs_new, predicted):
	#print('%r => %s' % (doc, target_names[category]))
	#f2.write(("\""+rest[i]+"\",\""+cuisine[i]+"\",\""+doc+"\",\""+target_names[category]+"\"\n"))
	#i=i+1

#print "Accuracy ( for testing set ): ",(np.mean(predicted == target_test))



text_clf = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', MultinomialNB())])
text_clf = text_clf.fit(train, target_train)

docs_test_2 = test
predicted_2 = text_clf.predict(docs_test_2)

text_clf_SGD = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, n_iter=5, random_state=42))])
text_clf_SGD.fit(train, target_train)
predicted_SGD = text_clf_SGD.predict(docs_test_2)

#print predicted_2
#docs_test_2=docs_new

for doc, category in zip(docs_test_2, predicted_2):
	#print('%r => %s ' % (doc, target_names[category]))
	ind_of_doc=docs_test_2.index(doc)
	#print "ind_of_doc",ind_of_doc
	actual_cat_target=target_test[ind_of_doc]
	#print "actual_cat_target",actual_cat_target
	actual_cat=target_names[actual_cat_target]
	#if(target_names[category] != actual_cat):
	#	print('%r => %s   actual_cat=%s' % (doc, target_names[category],actual_cat))

print "Accuracy in Naive Bayes ( for testing set ): ",(np.mean(predicted_2 == target_test))
print "Accuracy in SGD ( for testing set ): ",(np.mean(predicted_SGD == target_test))
f2.close()



def CategorizeReviewNVB(new_review):
	print "Using naive_bayes"
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

	for doc, category in zip(new_review, predicted):
		print('%r => %s ' % (doc, target_names[category]))

	frequencies_rev = Counter(predicted)
	total=frequencies_rev[0]+frequencies_rev[1]+frequencies_rev[2]+frequencies_rev[3]
	print "This review talks about : "
	print target_names[0],(frequencies_rev[0]/total)*100,"%"
	print target_names[1],(frequencies_rev[1]/total)*100,"%"
	print target_names[2],(frequencies_rev[2]/total)*100,"%"
	print target_names[3],(frequencies_rev[3]/total)*100,"%"

	return predicted,new_review


def CategorizeReviewSGD(new_review):
	print "using SGD"
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
	predicted = text_clf_SGD.predict(new_review)
	#print predicted

	for doc, category in zip(new_review, predicted):
		print('%r => %s ' % (doc, target_names[category]))

	frequencies_rev = Counter(predicted)
	total=frequencies_rev[0]+frequencies_rev[1]+frequencies_rev[2]+frequencies_rev[3]
	print "This review talks about : "
	print target_names[0],(frequencies_rev[0]/total)*100,"%"
	print target_names[1],(frequencies_rev[1]/total)*100,"%"
	print target_names[2],(frequencies_rev[2]/total)*100,"%"
	print target_names[3],(frequencies_rev[3]/total)*100,"%"

	return predicted,new_review


doc="Had been to this place with friends in the afternoon. The staff was friendly and cooperative. The food was excellent. Had ordered pizza and pan cakes, both of which were tasty. What I loved the most is the ambience."
print "test review"
print doc
#print type(doc)
pred,rev=CategorizeReviewNVB(doc)
pred2,rev2=CategorizeReviewSGD(doc)


fpath=os.path.join("data", "categorized_reviews.txt")
f=open(fpath,'r')

fpath2=os.path.join("data", "categorized_reviews_sentences.txt")
f2=open(fpath2,'a+')
for row in f:
	row=row.rstrip()
	row=row.split('"')
	if(len(row)==7):
		rest=row[1]
		cuisine=row[3]
		rev=row[5]
		#print rev
		#pred,rev=CategorizeReviewSGD(rev)
		#for cat,r in zip(pred,rev):
			#print r,":",target_names[cat]
			#f2.write("\""+rest+"\",\""+cuisine+"\",\""+r+"\",\""+target_names[cat]+"\"\n")

f.close()
f2.close()