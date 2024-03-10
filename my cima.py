import requests
import time
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re

i=0
while 1:
 f1 = open("tri.txt","w")
 req = requests.get("https://mycima.is/AjaxCenter/MoreEpisodes/house-of-the-dragon/"+ str(i)+ "/").j
 i=i+39
 soup = BeautifulSoup(req.text , "html.parser")
 #print(soup)
 link = soup.find_all("a")
 if len(link) == 1:
     #time.sleep(15)
     break
 print(link)
 for ii in link:
  e = ii["href"][2:-4]
  #print(e)
  rat=urlparse(e)  
  ep = (rat[0] +"://" +rat[2][4:])
  print(ep)
  req1 = requests.get(ep)
  soup1 = BeautifulSoup(req1.text , "html.parser")
  a = soup1.find_all("ul","List--Download--Mycima--Single")[0]
  print(len(a))
  epl = a.find("a")["href"]
  print (epl)
   
  
 #    epr = requests.get(ep)
 #   eps = BeautifulSoup(epr.text ,"html.parser" )
  #  epl = eps.find("a",{"class":"hoverable activable"})
   # print(epl)  