from cgitb import html
import requests
from bs4 import BeautifulSoup
import yt_dlp
import time 
list = []
def format_selector(ctx):
    """ Select the best video and the best audio that won't result in an mkv.
    NOTE: This is just an example and does not handle all cases """

    # formats are already sorted worst to best
    formats = ctx.get('formats')[::-1]

    # acodec='none' means there is no audio
    best_video = next(f for f in formats
                      if f['vcodec'] != 'none' and f['acodec'] == 'none')

    # find compatible audio extension
    audio_ext = {'mp4': 'm4a', 'webm': 'webm'}[best_video['ext']]
    # vcodec='none' means there is no video
    best_audio = next(f for f in formats if (
        f['acodec'] != 'none' and f['vcodec'] == 'none' and f['ext'] == audio_ext))

    # These are the minimum required fields for a merged format
    yield {
        'format_id': f'{best_video["format_id"]}+{best_audio["format_id"]}',
        'ext': best_video['ext'],
        'requested_formats': [best_video, best_audio],
        # Must be + separated list of protocols
        'protocol': f'{best_video["protocol"]}+{best_audio["protocol"]}'
    }
ydl_opts = {'format': format_selector,}

headers = { "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42"}
with requests.session() as s:
 r = s.get(str(input("enter course link ")), headers=headers)
 soup = BeautifulSoup(r.text , "html.parser").find("select" , {"id" : "srcs"} )
 #print(soup)

 x =BeautifulSoup(str(soup) , "html.parser").find_all("option")
 for i in x:
  z= BeautifulSoup(str(i) , "html.parser").find("option")["value"]
  if str(z) != str("0") :
   print (i.text+'https://youtu.be/'+z + "\n")#
   list.append(str('https://youtu.be/'+z + "\n"))
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
 ydl.download(list)
 print("end")