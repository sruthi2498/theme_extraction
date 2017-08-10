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

driver.get('https://www.tripadvisor.in/Hotels-g297628-Bengaluru_Bangalore_District_Karnataka-Hotels.html')
driver.implicitly_wait(50)

'''
def ListOfHotels():
	all_hotels=driver.find_elements_by_xpath("//div[@class='listing_title']/a")
	for i in range(0,len(all_hotels)):
		all_hotels=driver.find_elements_by_xpath("//div[@class='listing_title']/a")
		all_hotels[i].click()
		#do stuff
		driver.back()
'''
try:
	
	next_exists=1
	while(next_exists==1):
		all_pages=driver.find_elements_by_xpath("//div[@class='pageNumbers']/a")
		current_page=driver.find_element_by_xpath("//div[@class='pageNumbers']/span").text
		next_pages=driver.find_element_by_xpath("//div[@class='pageNumbers']/a[@class='pageNum taLnk']")
		print next_pages[0].text
		print current_page
		next_exists=0


except Exception as e:
    print e