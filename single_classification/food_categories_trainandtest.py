from __future__ import division
import os
import random
import re

fpath=os.path.join("data", "training_data_set.txt")
f=open(fpath,'r')
fpath2=os.path.join("data", "food_data_set.txt")
f2=open(fpath2,'a+')
i=0
for row in f:
	i=i+1
	if(i>=902):
		r=row
		row=row.rstrip()
		row=row.split('"')
		if(len(row)==9):
			rest=row[1]
			cuisine=row[3]
			rev=row[5]
			cat=row[7]
			if(cat=='food'):
				f2.write(r)


Cuisines=['north indian', 'italian', 'salad', 'healthy', 'cafe', 'desserts', 'bakery', 'continental', 'european', 'burger', 'thai', 'pizza', 'mediterranean', 'andhra', 'biryani', 'seafood', 'fast food', 'street food', 'american', 'chinese', 'asian', 'vietnamese', 'indonesian', 'kerala', 'mughlai', 'arabian', 'juices', 'south indian', 'beverages', 'steak', 'mexican']
f.close()