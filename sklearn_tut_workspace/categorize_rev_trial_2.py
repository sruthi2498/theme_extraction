import os
fpath=os.path.join("data", "categorized_reviews.txt")
f=open(fpath,'r')
fpath2=os.path.join("data", "categorized_reviews_sentences.txt")

f2=open(fpath2,'r')

fpath3=os.path.join("data", "categorized_reviews_sentences_2.txt")
f3=open(fpath3,'a+')

count =0
#categories=['food','ambience','price','service']
food_count=0
ambi_count=0
price_count=0
serv_count=0
other_count=0
for row in f2:
	r=row
	row=row.rstrip()
	row=row.split('"')
	cat=row[7]
	
	if(row[7]=="delivery"):
		r=r.replace('"delivery"','"other"')
		print r
	if(row[7]=="order"):
		r=r.replace('"order"','"other"')
		print r
	row=r
	
	
	if(cat=='food'):
		#print cat
		food_count=food_count+1
		if(food_count<=77):
			f3.write(r)
	elif(cat=='ambience'):
		#print cat
		ambi_count=ambi_count+1
		if(ambi_count<=77):
			f3.write(r)
	elif(cat=='price'):
		#print cat
		price_count=price_count+1
		if(price_count<=77):
			f3.write(r)
	elif(cat=='service'):
		#print cat
		serv_count=serv_count+1
		if(serv_count<=77):
			f3.write(r)
	else:

		#print cat
		other_count=other_count+1
		if(other_count<=77):
			f3.write(r)
		
	



print food_count,ambi_count,price_count,serv_count,other_count
f.close()
f2.close()