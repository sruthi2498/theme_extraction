import os

fpath1=os.path.join("data", "training_data_set.txt")
fpath1=os.path.join("data", "testing_data_set_200.txt")
f1=open(fpath1,'r')
cat=[]
cat_dict={}
cat_types=[]
categories=['filler', 'taste', 'price', 'tax', 'quantity', 'location', 'food', 'seating', 'atmosphere', 'service', 'waiters', 'company', 'decor', 'rating', 'menu', 'presentation', 'bar', 'waiting time', 'delivery', 'sanitation', 'opening time']
for row in f1:
	row=row.rstrip()
	row=row.split('"')
	if(len(row)<9):
		print row
	if(len(row)==9):
		t=row[7]
		t=t.split(',')
		t=sorted(t)
		if t not in cat_types:
			cat_types.append(t)
		if(len(t)>2):
			print row
		for x in t:
			if x not in cat:
				if(x=='ambience'):
					print row
				cat.append(x)
print cat
print categories
for c in categories:
	if c not in cat:
		print c
List={}
for cat in cat_types:
	
	cat=' '.join(cat)
	a=[]
	List[cat]=a
'''

fpath=os.path.join("data", "training_data_set_100.txt")
f=open(fpath,'r')
for row in f:
	rev=row
	row=row.rstrip()
	row=row.split('"')
	if(len(row)==9):
		t=row[7]
		t=t.split(',')
		t=sorted(t)
		t=' '.join(t)
		List[t].append(rev)

for key,val in List.iteritems():
	print key,":",len(val)

f.close()
'''
