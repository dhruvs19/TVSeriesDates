#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import os

url = ['http://www.imdb.com/title/tt3749900/episodes?ref_=tt_ov_epl','http://www.imdb.com/title/tt3107288/episodes?ref_=tt_ov_epl','http://www.imdb.com/title/tt2193021/episodes?ref_=tt_ov_epl','http://www.imdb.com/title/tt2364582/episodes?ref_=tt_ov_epl','http://www.imdb.com/title/tt4532368/episodes','http://www.imdb.com/title/tt1520211/episodes','http://www.imdb.com/title/tt4016454/episodes?season=2&ref_=tt_eps_sn_2','http://www.imdb.com/title/tt2306299/episodes?season=4&ref_=tt_eps_sn_4']

for i in url:
	print('\n')
	page = requests.get(i)
	
	if page.status_code == 200:
		soup = BeautifulSoup(page.text,"html.parser")
		sname = soup.find_all("a", class_="subnav_heading")
	
		for i in sname:
			print('**********  ' + i.text + '  **********\n')
		
		date = soup.find_all("div", class_="airdate")

		for d in date:
			if '2017' in d.text:
				parenti = d.parent.parent
				episodename = parenti.find_all("div", class_="hover-over-image")
				ename = episodename[0].text
				
				if "Add Image" in ename:
					vari = ename.replace("Add Image",'',1)
					print(vari.strip() + "      " + d.text.strip())
				else:	
					print(ename.strip() + "      " + d.text.strip())
			
	else: 
		print("Oops! An Error Occurred") 


print("\n\n")		
os.system("pause")