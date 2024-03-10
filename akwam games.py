import requests
from bs4 import BeautifulSoup
import pyperclip
s= requests.session()
headers = {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"}
a =BeautifulSoup( s.get(input("enter game link ") , headers=headers).text , "html.parser" ).findAll( "a" , {"class": "link-btn link-download d-flex align-items-center px-3"})
clip = ""
for i in a: 
    link = BeautifulSoup(str(i), "html.parser").find("a")["href"]
    url = BeautifulSoup( s.get(link , headers=headers).text , "html.parser" ).find("a" , {"class":"download-link"})["href"]
    part = BeautifulSoup(s.get(url , headers=headers).text , "html.parser").find("a" , {"class":"link btn btn-light"})["href"]
    clip = clip + "\n"+ part  ;print(part)
pyperclip.copy(clip);pyperclip.paste()
input("press to exit")
