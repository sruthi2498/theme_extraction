from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException        
import os
from pyvirtualdisplay import Display

from bs4 import BeautifulSoup
'''
profile = FirefoxProfile('/home/sruthi/.mozilla/firefox')
driver = webdriver.Firefox(profile)
driver.get("https://www.zomato.com/bangalore")
driver.implicitly_wait(7)

display = Display(visible=0, size=(800, 800))  
display.start()
print "here"
browser = webdriver.Chrome()
print "ok"
browser.get('http://www.google.com')'''

fpath=os.path.join("data", "output.csv")
f=open(fpath,'a+')

chrome_path="/usr/local/bin/chromedriver" 

driver=webdriver.Chrome(chrome_path)

driver.maximize_window()

driver.get('http://www.zomato.com')
driver.implicitly_wait(50)
try:
	
	all_elems=driver.find_elements_by_xpath("//a[@class='col-l-1by3 col-s-8 pbot0']")

	#print len(all_elems)
	for i in range(29,len(all_elems)):
		all_elems=driver.find_elements_by_xpath("//a[@class='col-l-1by3 col-s-8 pbot0']")
		print "location"
		all_elems[i].click()
		driver.implicitly_wait(30)
		see_more=driver.find_elements_by_xpath("//a[@class='zred']")
		#print len(see_more)
		for j in range(0,len(see_more)):
			see_more=driver.find_elements_by_xpath("//a[@class='zred']")
			print "see more"
			see_more[j].click()
			driver.implicitly_wait(30)
			each_rest=driver.find_elements_by_xpath("//a[@class='result-title hover_feedback zred bold ln24   fontsize0 ']")

			#print len(each_rest)
			for k in range(0,len(each_rest)):
				each_rest=driver.find_elements_by_xpath("//a[@class='result-title hover_feedback zred bold ln24   fontsize0 ']")
				print "each rest"
				each_rest[k].click()
				driver.implicitly_wait(30)

				name_of_rest=driver.find_element_by_xpath("//a[@class='ui large header left']").text
				name_of_rest=name_of_rest.encode('ascii', 'ignore').decode('ascii')
				#print name_of_rest
				cuisines=driver.find_element_by_xpath("//div[@class='res-info-cuisines clearfix']").text
				cuisines=cuisines.encode('ascii', 'ignore').decode('ascii')
				#print cuisines
				rev=driver.find_element_by_xpath("//*[contains(text(), 'Reviews')]")
				rev.click()
				all_rev=driver.find_element_by_xpath("//*[contains(text(), 'All Reviews')]")
				print "all rev button"
				all_rev.click()
				print "clicked"
				#load_more=driver.find_element_by_xpath("//div[@class='load-more bold ttupper tac cursor-pointer fontsize2']/span[@class='zred']")
				#print type(load_more)
				#load_more.click()
				driver.implicitly_wait(30)
				#print "clicked"
				exists=1;
				while(exists==1):
					#load_more.click()
					load_more=driver.find_elements_by_xpath("//div[@class='load-more bold ttupper tac cursor-pointer fontsize2']/span[@class='zred']")
					print len(load_more)
					if(len(load_more)>=1):
						load_more[0].click()
					else:
						exists=0
					'''try:
						driver.find_element_by_xpath("//div[@class='load-more bold ttupper tac cursor-pointer fontsize2']/span[@class='zred']").click()
						print "load more"
					except:
						print "unable to load"
						break'''


				all_reviews=driver.find_elements_by_xpath("//div[@class='rev-text mbot0 ']")

				print "all reviews"
				#print len(all_rev)
				for l in range(0,len(all_reviews)):
					rev=driver.find_elements_by_xpath("//div[@class='rev-text mbot0 ']")[l].text
					rev=BeautifulSoup(rev,"lxml").text
					rev=rev.encode('ascii', 'ignore').decode('ascii')
					rev=rev.replace('RATED','')
					rev=rev.replace('"','')
					rev=rev.replace('\n','')
					rev=rev.replace('"\n','')
					#print rev
					rev=rev.rstrip()
					#print rev
					#print rev
					f.write("\""+name_of_rest+"\",\""+cuisines+"\",\""+rev+"\"\n")
				driver.back()
				driver.back()
			driver.back()
		driver.back()
	print "does it work?"
	driver.implicitly_wait(7)
except Exception as e:
    print e
#driver.quit()
print "done"
f.close()