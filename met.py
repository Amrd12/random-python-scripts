from cgitb import html
import requests
from bs4 import BeautifulSoup
import yt_dlp
import re
import webbrowser
from urllib.request import urlopen

list = []
id = []

login_url = "https://els-engmet.com/login/"
payload = {
"log" : "amr60608",
"pwd" : "i1c2oeby",
"wp-submit" : "دخول",
"redirect_to": "https://els-engmet.com/"
}
headers = { "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42"}
with requests.session() as s:
 log_in = s.post(url = login_url , data = payload , headers=headers)
 r = s.get("https://els-engmet.com/courses/computer-applications-2023/", headers=headers)
 soup = BeautifulSoup(r.text , "html.parser").find_all("div" , {"class" : "tutor-course-lesson"} )
 for i in soup:
  x =BeautifulSoup(str(i) , "html.parser").find("a")["href"]
  print(i.text )
  lec = s.get(str(x) , headers = headers)
  z= BeautifulSoup(lec.text , "html.parser").find("iframe",{"allow" : "autoplay"})["src"]
  print ('video ',  z ,'\n')
  list.append(z)
  id.append(z.split('/')[-1].split('?')[0])

# Convert the list of video IDs to a comma-separated string
videoIds = ','.join(id)

# Construct the playlist URL
playlistUrl = "http://www.youtube.com/watch_videos?video_ids=" + videoIds

response = urlopen(playlistUrl)
playListLink = response.geturl()
# print playListLink

playListLink = playListLink.split('list=')[1]
# print playListLink

playListURL = "https://www.youtube.com/playlist?list="+playListLink+"&disable_polymer=true"
# Open the playlist URL in a web browser
webbrowser.open(playlistUrl)
