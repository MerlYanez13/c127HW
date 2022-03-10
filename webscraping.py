from selenium import webdriver
from bs4 import BeautifulSoup
import time 
import csv
import requests
import pandas as pd
START_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

page=requests.get(START_URL)
soup=BeautifulSoup(page.text,"html.parser")
startTable=soup.find('table')
tableList=[]
tableRows=startTable.find_all('tr')
for tr in tableRows:
    td=tr.find_all('td')
    row=[i.text.rstrip() for i in td]
    tableList.append(row)
Name=[]
Distance=[]
Mass=[]
Radius=[]
Lumoninosity=[]
for i in range(1, len(tableList)):
    Name.append(tableList[i][1])
    Distance.append(tableList[i][3])
    Mass.append(tableList[i][5])
    Radius.append(tableList[i][6])
    Lumoninosity.append(tableList[i][7])
df=pd.DataFrame(list(zip(Name,Distance,Mass,Radius,Lumoninosity)),columns=['star_name','distance',"mass",'radius','Lumoninosity'])
df.to_csv('webscraping.csv')