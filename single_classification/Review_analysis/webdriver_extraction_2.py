from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException        
import os
from pyvirtualdisplay import Display
from bs4 import BeautifulSoup
'''
fpath=os.path.join("data", "output.csv")

f=open(fpath,'a+')'''

chrome_path="/usr/local/bin/chromedriver" 

driver=webdriver.Chrome(chrome_path)

driver.maximize_window()

driver.get('http://www.mouthshut.com/restaurants/bangalore')
driver.implicitly_wait(50)
try:
	exists=1
	while(exists==1):
		all_elems=driver.find_elements_by_xpath("//div[@class='rtitle']/a")
		for i in range(0,len(all_elems)):
			print "each rest"
			all_elems=driver.find_elements_by_xpath("//div[@class='rtitle']/a")
			all_elems[i].click()
			name_of_rest=driver.find_element_by_xpath("//h2[@class='pull-left']").text
			name_of_rest=name_of_rest.encode('ascii', 'ignore').decode('ascii')
			print name_of_rest
			next_exists=1
			while(next_exists==1):
				all_revs=driver.find_elements_by_xpath("//div[@class='more reviewdata']")
				for j in range(0,len(all_revs)):
					all_revs=driver.find_elements_by_xpath("//div[@class='more reviewdata']")
					rev=all_revs[j].text
					rev=BeautifulSoup(rev,"lxml").text
					rev=rev.encode('ascii', 'ignore').decode('ascii')
					rev=rev.replace('RATED','')
					rev=rev.replace('"','')
					rev=rev.replace('\n','')
					#print rev
				next2=driver.find_elements_by_xpath("//li[@class='next']/a")
				next_counter=0
				print len(next2)
				if(len(next2)>=1):
					next2[0].click()
					next_counter=next_counter+1
					print "next count ",next_counter,"clicking on next"
				else:
					next_counter=0
					while(next_exists):
						"next count ",next_counter,"going back"
						driver.back()
						next_counter=next_counter-1
						#"next count ",next_counter,"going back"



			#print "back to main page"
			driver.back()
		next=driver.find_elements_by_xpath("//li[@class='next']/a")
		#print "next "+len(next)
		print len(next)
		if(len(next)>=1):
			next[0].click()
		else:
			exists=0

		
except Exception as e:
    print e
#driver.quit()
print "done"
#f.close()