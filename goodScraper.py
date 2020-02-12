# Web scraper for Good on You ratings
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'https://directory.goodonyou.eco/brand/bario-neal'

driver = webdriver.Firefox()
driver.get(url)

# parsing through the page
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())

driver.close()
# # getting table elements
# table_body=page_soup.find('tbody')
# rows= table_body.find_all('tr')
# result = []
# for i in range(len(rows)):
# 	cols=rows[i].find_all('td')
# 	result.append(cols)
#
# # creating dictionary to save everything into
# master={}
#
# #get image infomrmation
# src= result[1][0].find('img')['src'][2:]
# master["image"]=src
#
# # looping through the text information
# for j in range(2,len(result)):
#
# 	key= page_soup.findAll("th",{"style":"white-space:nowrap;padding-right:0.65em;"})[j-2].string
# 	classname= result[j][0].find_all("div",{"class":"plainlist"})
#
# 	if classname == []: # one item
# 		if not result[j][0].find('a'):
# 			body=str(result[j][0])[4:-5]
#
# 		else:
# 			body = result[j][0].find('a').string
#
# 	else: # list of items
# 		body = []
# 		string= result[j][0].find_all('li')
# 		for i in range(len(string)):
# 			s = string[i].string
# 			body.append(s)
#
# 	master[key]=body
#
# #cleaning up the dictionary, deleting information that we do not want
# to_be_deleted=[]
# for key in master:
# 	if isinstance(master[key],list) and len(master[key])==1:
# 		to_be_deleted.append(key)
# 	if str(master[key])[0] == "[":
# 	  	to_be_deleted.append(key)
# for key in to_be_deleted:
# 	del master[key]
