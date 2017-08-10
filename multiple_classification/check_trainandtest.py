import os

fpath1=os.path.join("data", "training_data_set.txt")
f1=open(fpath1,'r')
train=[]
for row in f1:
	row=row.rstrip()
	train.append(row)

fpath2=os.path.join("data", "testing_data_set_200.txt")
f2=open(fpath2,'r')
i=0
test=[]
for row in f2:
	row=row.rstrip()
	test.append(row)

for row in test:
	if row in train:
		print i,row
	i=i+1