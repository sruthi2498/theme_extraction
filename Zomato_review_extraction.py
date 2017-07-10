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
