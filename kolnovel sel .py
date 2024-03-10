from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import os
import re
import urllib.parse

def naming(string):
    cleaned_string = re.sub(r'[/*?:"<>|]', "", string)
    utf8_encoded = urllib.parse.unquote(cleaned_string)
    return utf8_encoded

def get_chapter(url):
    driver.get(url)
    driver.implicitly_wait(10)
    paragraphs = driver.execute_script("""
        const div = document.getElementsByClassName("epcontent entry-content")[0].getElementsByTagName("p");
        let pragraphs = "";
        
        if (div.length > 10) {
            Array.from(div).forEach(p => {
                if (getComputedStyle(p).bottom !== "-999px") {
                    pragraphs += p.textContent + "\\n";
                }
            });
        } else {
            const h4Elements = document.getElementsByClassName("epcontent entry-content")[0].getElementsByTagName("h4");
            Array.from(h4Elements).forEach(h4 => {
                pragraphs += h4.textContent + "\\n";
            });
        }
        
        return pragraphs;
    """)
    driver.close()
    return paragraphs

def novel(url):
    chap = []
    s = requests.session()
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"}
    soup = BeautifulSoup(s.get(url ,headers=headers ).text  , "html.parser").find("div" , {"class":"bixbox bxcl epcheck"}).findAll("li")
    for div in reversed(soup):
        chap.append({"number" : div.find("div" , {"class" : "epl-num"}).text 
                   , "name" : div.find("div" , {"class" : "epl-title"}).text
                   , "url" :div.find("a")["href"]})
    
    return chap

def main():
   url = input("Enter novel links ")
   name = naming(str(url[28:-1]))
   path = f"C:\\manga\\{name}"
   if not os.path.exists(path): os.makedirs(path)
   file = open(f"{path}\\{name}.txt" , "w", encoding="utf-8")
   nov =  novel(url)
   print(f"found {len(nov)} chapter")
   for i,link in enumerate(nov):
       print(i)
       make_driver()
       text = get_chapter(link["url"]) or ""
       driver.quit()
       contant = f"{i}  {link['number']} {link['name']} \n \n {text}\n \n \n"
       file.write(contant)

def make_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--log-level=3")   # This line enables headless mode
    global driver
    driver = webdriver.Chrome(options=chrome_options)

if __name__ == "__main__":
    main()