import requests
import os
import csv
import pandas as pd
from pprint import pprint
from bs4 import BeautifulSoup


clat=12.871371
clon=77.594501
zomatoKey = "46678c847517af16b7f56dafd773bcdb"

fpath=os.path.join("data", "output.csv")
f=open(fpath,'a+')

#*************************************************************************************************************************************8

'''#GET A LIST OF CATEGORIES 
CategoriesUrl= "https://developers.zomato.com/api/v2.1/categories?"
header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": zomatoKey}

categories= requests.get(CategoriesUrl, headers=header)
print r.status_code
print r.headers
print r.content
r.elapsed       # returns datetime.timedelta(0, 1, 666890)
r.url           # returns 'https://tutsplus.com/'
 
r.history      # returns [<Response [301]>, <Response [301]>]
 
r.headers['Content-Type']
#print categories.json()
CatJson=categories.json()
#print CatJson.items()
#print type(CatJson)
ListOfCategories=[]
#print CatJson.values()
for V in CatJson.values():
    for i in V:
        for V2 in i.values():
            #print type(V2)
            #print V2
            for key,val in V2.items():
                if(key=='name'):
                    #print val
                    ListOfCategories.append(val)
#print ListOfCategories'''
#*************************************************************************************************************************************8

#GET A LIST OF RES_IDS
header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": zomatoKey}

SearchUrl= "https://developers.zomato.com/api/v2.1/search"
SearchResults= requests.get(SearchUrl, headers=header)
SearchJson=SearchResults.json()
#print SearchJson["results_found"]
ListOfResIds=[]
n=len(SearchJson["restaurants"])
for i in range(n):
    #print SearchJson["restaurants"][i]["restaurant"]["R"]["res_id"]
    ListOfResIds.append(SearchJson["restaurants"][i]["restaurant"]["R"]["res_id"])
#print ListOfResIds

#*************************************************************************************************************************************8

#f.write("\n")

for id in ListOfResIds:
    rid=str(id)
    RestUrl="https://developers.zomato.com/api/v2.1/restaurant?res_id="+rid
    RestResults= requests.get(RestUrl, headers=header)
    RestJson=RestResults.json()
    #print RestJson["name"]
    name=RestJson["name"]
    cuisines=RestJson["cuisines"]

    RevUrl="https://developers.zomato.com/api/v2.1/reviews?res_id="+rid
    RevResults= requests.get(RevUrl, headers=header)
    RevJson=RevResults.json()
    n=len(RevJson["user_reviews"])
    for i in range(n):
        rev=RevJson["user_reviews"][i]["review"]["review_text"]
        rev = BeautifulSoup(rev,"lxml").text
        
        reid=RevJson["user_reviews"][i]["review"]["id"]
        '''df=pd.read_csv(fpath)
        #print df.loc[i, "revid"]
        allrevids=df.loc[1:,"revid"]
        present=False
        print type(str(reid))
        print type(str(allrevids))
        for r in allrevids:
            if(str(r)==str(reid)):
                prsent=True
                break
        #print rev
        if(present==False):'''
        f.write("\""+name+"\",\""+rid+"\",\""+cuisines+"\",\""+rev+"\",\""+reid+"\"\n")

        
f.close()