import requests
import json
#import pyperclip
import subprocess
x=2
while x>1:
  name = input('Enter anime link ') ;  name =name[31:]    ;      i=1        ;      j=0     ;     f = str(name)+".txt"      ;      f1 = open(f,"w")     ;    clip = ""
  while 1:
    #print("hoshi-no-samidare")
    link = "https://api.animeiat.co/v1/episode/"+ name +"-episode-" + str(i) 
    i+=1
    #print (link)
    req = requests.get(link)
    if req.status_code == 404 or req.status_code == 500:
      j+=1
      if j==3:
       break
    else: 
      j=0
      data = json.loads(req.text)
      #print(data)
      id = data["data"]["video"]["slug"]
      #print (id)
      #print(id)    https://api.animeiat.co/v1/video/e3ee7d4f-b3ff-49c3-b058-4bab1e94c98c/download 
      ep = json.loads(requests.get( "https://api.animeiat.co/v1/video/"+ id  + "/download").text)
      try:
        video = ep["data"][0]["file"]
      except:
        video = ep["data"][1]["file"]
      clip = clip + video + "\n"
      print(video)
      process = subprocess.Popen(["C:/Program Files/FreeDownloadManager.ORG/Free Download Manager/fdm.exe", ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      output, error = process.communicate()
      f1.write(video+"\n")
  #pyperclip.copy(clip)
  print("end \n\n\n\n\n\n")
  if (input('Press t to try again') != "t") : x=1