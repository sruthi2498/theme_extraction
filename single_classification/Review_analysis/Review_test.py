import os
import nltk
import sys
import random
import csv
import re
reload(sys)
sys.setdefaultencoding('utf8')
from nltk.corpus import movie_reviews
fpath=os.path.join("data", "output.csv")
fpath_neg=os.path.join("data", "negative_words.txt")
fpath_pos=os.path.join("data", "positive_words.txt")

corpus = nltk.corpus.reader.plaintext.PlaintextCorpusReader(".", fpath)
sents=corpus.sents()

	#print m
Reviews=[]
f=open(fpath,'r')


for row in f:
	contents=row.split(',')
	for elem in contents:
		elem=elem.replace('"','')
	#print len(Reviews)
	#Reviews[i]["RestName"]=contents[0]
	cuisines=[]
	for i in range(1,len(contents)-1):
		cuisines.append(contents[i])
	#Reviews[i]["cuisines"]=cuisines
	revs=contents[len(contents)-1]
	revs=revs.split('.')
	rev=[]
	for r in revs:
		r=r.rstrip()
		rev.append({"sentence":r,"pos":0,"neg":0})
	Reviews.append({"entire_rev":contents[len(contents)-1],"rest_name":contents[0],"cuisines":cuisines,"rev":rev,"total_pos":0,"total_neg":0})
	
neg_file=open(fpath_neg,'r')
pos_file=open(fpath_pos,'r')
neg_words=[]
pos_words=[]
for r in neg_file:
	r=r.rstrip()
	neg_words.append(r)
for r in pos_file:
	r=r.rstrip()
	pos_words.append(r)
for i in range(0,len(Reviews)):
	number_of_revs=len(Reviews[i]["rev"])
	for j in range(0,number_of_revs):
		Words=Reviews[i]["rev"][j]["sentence"].split()
		for word in Words:
			if word in neg_words:
				Reviews[i]["rev"][j]["neg"]+=1
				Reviews[i]["total_neg"]+=1
			if word in pos_words:
				Reviews[i]["rev"][j]["pos"]+=1
				Reviews[i]["total_pos"]+=1

#print Reviews[7]
Test_List=[]

for i in range(0,len(Reviews)):
	number_of_revs=len(Reviews[i]["rev"])
	if Reviews[i]["total_pos"]>=Reviews[i]["total_neg"]:
		Test_List.append((Reviews[i]["entire_rev"],"pos"))
	else:
		Test_List.append((Reviews[i]["entire_rev"],"neg"))

def CreateListWithSentiment(List):
	LWS=[]
	for (words, sentiment) in List:
		#print "words ",words,"sentiment ",sentiment
		SplitWords=words.split()
		words_filtered = [e.lower() for e in SplitWords if len(e) >= 3]
		#print words_filtered
		LWS.append((words_filtered, sentiment))
	return LWS;

ListWithSent=CreateListWithSentiment(Test_List)
#print ListWithSent[0]


def get_words(List):
	all_words = []
	for (words, sentiment) in List:
		all_words.extend(words)
	return all_words

Words=get_words(ListWithSent)
#print Words

def get_word_features(wordlist):
	wordlist = nltk.FreqDist(wordlist)
	
	word_features = wordlist.keys()
	return word_features

WordFeatures=get_word_features(Words)

print WordFeatures

def extract_features(document):
	document_words = set(document)
	features = {}
	for word in WordFeatures:
		features['contains(%s)' % word] = (word in document_words)
	return features


training_set = nltk.classify.apply_features(extract_features, ListWithSent)

#print training_set

classifier = nltk.NaiveBayesClassifier.train(training_set)

#print label_probdist.prob('positive')

tweet='You are not good'
print classifier.classify(extract_features(tweet.split()))

classifier.show_most_informative_features(5)