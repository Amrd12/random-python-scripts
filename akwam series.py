import requests
from bs4 import BeautifulSoup
import pyperclip
s= requests.session()
headers = {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"}
a =BeautifulSoup( s.get(input("enter series link ") , headers=headers).text , "html.parser" ).find_all("div", {"class":"bg-primary2 p-4 col-lg-4 col-md-6 col-12", "style": "margin-bottom: 2px"})#.findAll( "a" , {"class": "text-white"})
clip = ""
for i in a.__reversed__(): 
    link = BeautifulSoup(str(i), "html.parser").find("a")["href"]
    url = BeautifulSoup( s.get(link , headers=headers).text , "html.parser" ).find("a" , {"class":"link-btn link-download d-flex align-items-center px-3"})["href"]
    part = BeautifulSoup(s.get(url , headers=headers).text , "html.parser").find("div" , {"class" : "content"}).find("a" , {"class":"download-link"})["href"]
    video = BeautifulSoup(s.get(part , headers=headers).text , "html.parser").find("a" , {"class":"link btn btn-light"})["href"]
    clip = clip + "\n"+ video  ;print(video)    
pyperclip.copy(clip);pyperclip.paste()
input("press to exit")

"""<div class="bg-primary2 p-4 col-lg-4 col-md-6 col-12" style="margin-bottom: 2px">
<h2 class="font-size-18 text-white mb-2">
<a class="text-white" href="https://akwam.cam/episode/71560/quantum-leap-Ø§ÙÙÙØ³Ù-Ø§ÙØ§ÙÙ/Ø§ÙØ­ÙÙØ©-10">Ø­ÙÙØ© 10 : ÙØ³ÙØ³Ù Quantum Leap Ø§ÙÙÙØ³Ù Ø§ÙØ§ÙÙ  Paging Dr. Song</a>
</h2>
<p class="entry-date font-size-12 text-muted mb-2">Ø§ÙØ«ÙØ§Ø«Ø§Ø¡ 10 ÙÙØ§ÙØ± 2023 - 02:03 ÙØ³Ø§Ø¡Ø§Ù</p>
<div class="row">
<div class="col-md-auto text-center pb-3 pb-md-0">
<a href="https://akwam.cam/episode/71560/quantum-leap-Ø§ÙÙÙØ³Ù-Ø§ÙØ§ÙÙ/Ø§ÙØ­ÙÙØ©-10">
<picture>
<img alt="10 : Paging Dr. Song" class="img-fluid" src="https://img.akwam.link/thumb/320x190/uploads/XsXSg.jpg"/>
</picture>
</a>
</div>
</div>
</div>"""