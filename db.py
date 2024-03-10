import sqlite3
from abc import ABC, abstractmethod
import json

#db main class controller
class db(ABC):
	def __init__(self,name,value):
		self.__name = name
		self.__value = value
		
	
	def makedb(self):
		con = sqlite3.connect("data.db")
		con.execute("""
		CREATE TABLE IF NOT EXISTS video (
		name text NOT NULL,
		link text,
		thumbnail text,
		down TEXT
		);""")
		con.execute("""
		CREATE TABLE IF NOT EXISTS playlist (
		name text NOT NULL,
		link text,
		thumbnail text,
		down TEXT
		);""")
		con.execute("""
		CREATE TABLE IF NOT EXISTS channel (
		name text NOT NULL,
		link text,
		thumbnail text
		);""")
		con.execute("""
		CREATE TABLE IF NOT EXISTS search (
		name text NOT NULL
		);""") 
		con.close()
	
	def check(self):
		con = sqlite3.connect("data.db")
		cursor = con.cursor()
		# Check if the table exists
		cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.__name}'")
		result = cursor.fetchone()
		con.close()
		# If result is not None, the table exists
		if result is None:
			self.makedb()

	@abstractmethod
	def get(self , condition= ""):
		self.check()
		con = sqlite3.connect("data.db")
		cursor = con.cursor()
		if not  condition =="":
			condition = "where "+ condition
		
		cursor.execute(f"SELECT * FROM {self.__name} " + condition)
		data = cursor.fetchall()
		con.close()
		return data
	
	@abstractmethod
	def insert(self, values):
		self.check()
		con = sqlite3.connect("data.db")
		con.execute(f"INSERT INTO {self.__name} VALUES {self.__value}",values)
		con.commit()
		con.close()

	@abstractmethod
	def delete(self,name, value):
		con = sqlite3.connect("data.db")
		con.execute(f"DELETE FROM {self.__name} WHERE {name} = '{value}'")
		con.commit()
		con.close()
	
	@abstractmethod
	def updated(self,new = "col = value",old="col = value"):
		self.check()
		con = sqlite3.connect("data.db")
		con.execute(f"update  {self.__name} set  {new} where {old}")
		con.commit()
		con.close()


class VideoDB(db):
	def __init__(self):
		super().__init__('video',"(?,?,?,?)")
	def get(self , condition = ""):
		data = super().get(condition=condition)
		items = []
		for i in data:
			items.append(video(i[0],i[1],i[2],i[3]))
		return items

	def insert(self, values = ("name","link","thumbnail","down")):
		super().insert(values)
	
	def delete(self,value):
		super().delete(name="link",value=value)
	def updated(self,tup):
		super().updated(new=f"name = '{tup[0]}'  , thumbnail = '{tup[2]}' , down = '{tup[3]}'" , old= f"link = '{tup[1]}'")

class video(VideoDB):
	def __init__(self,name=None,link=None,thumbnail=None,down="",data=None):
		if data is not None  and type(data) == json:
			self.tup = (data[name],data[link],data[thumbnail],data[down])
		else:
			self.tup = (name,link,thumbnail,down)
		self.name = self.tup[0]
		self.link = self.tup[1]
		self.thumbnail = self.tup[2]
		self.down = self.tup[3]
		super().__init__()
	def insert(self):
		super().insert(self.tup)#(self.name,self.link,self.down))
	def delete(self):
		super().delete(self.link)
	def updated(self, name =None,thumbnail= None, down= None):
		if name  is None: name = self.name
		if thumbnail  is None: thumbnail = self.thumbnail
		if down  is None: down = self.down
		self.tup = (name,self.link,thumbnail,down)
		self.name = self.tup[0]
		self.link = self.tup[1]
		self.thumbnail = self.tup[2]
		self.down = self.tup[3]
		super().updated(self.tup)
	def __str__(self) :
		data = {
			'type': 'video',
			'name': self.name,
			'link': self.link,
			'thumbnail': self.thumbnail,
			'down': self.down
		}
		return json.dumps(data, indent=4)
	def isfound(self):
		data = super().get(f"link = '{self.link}'")
		return bool(len(data))

class SearchDB(db):
	def __init__(self):
		super().__init__('search',"(?)")
	def get(self , condition =""):
		data = super().get(condition)
		items = []
		for i in data:
			items.append(search(i[0]))
		return items
	def insert(self, values = ("",)):
		super().insert(values)
	def delete(self,value):
		super().delete(name="name",value=value)
	def updated(self,tup):
		super().updated(new=f"name = '{(tup[1])}'" , old= f"name = '{(tup[0])}'")

class search(SearchDB):
	def __init__(self,name):
		self.tup = (name,)
		self.name = self.tup[0]
		super().__init__()
	def insert(self):
		super().insert(self.tup)
	def delete(self):
		super().delete(self.name)
	def updated(self, name):
		super().updated((self.name,name))
		self.tup=(name,)
		self.name = self.tup[0]
	def __str__(self) :
		return f"{self.name}"
	def isfound(self):
		data = super().get(f"name = '{self.name}'")
		return bool(len(data))

class PlaylistDB(db):
	def __init__(self):
		super().__init__('playlist',"(?,?,?,?)")
	def get(self,condition=""):
		data = super().get(condition)
		items = []
		for i in data:
			items.append(playlist(i[0],i[1],i[2],i[3]))
		return items
	def insert(self, values = ("name","link","thumbnail","down")):
		super().insert(values)
	def delete(self,value):
		super().delete(name="link",value=value)
	def updated(self,tup):
		super().updated(new=f"name = '{tup[0]}' ,thumbnail='{tup[2]}' , down = '{tup[3]}'" , old= f"link = '{tup[1]}'")

class playlist(PlaylistDB):
	def __init__(self,name,link,thumbnail,down=""):
		self.tup = (name,link,thumbnail,down)
		self.name = self.tup[0]
		self.link = self.tup[1]
		self.thumbnail = self.tup[2]
		self.down = self.tup[3]
		super().__init__()
	def insert(self):
		super().insert(self.tup)#(self.name,self.link,self.down))
	def delete(self):
		super().delete(self.link)
	def updated(self, name =None,thumbnail= None, down= None):
		if name  is None: name = self.name
		if thumbnail  is None: thumbnail = self.thumbnail
		if down  is None: down = self.down
		self.tup = (name,self.link,thumbnail,down)
		self.name = self.tup[0]
		self.link = self.tup[1]
		self.thumbnail = self.tup[2]
		self.down = self.tup[3]
		super().updated(self.tup)
	def __str__(self) :
		data = {
			'type': 'playlist',
			'name': self.name,
			'link': self.link,
			'thumbnail': self.thumbnail,
			'down': self.down
		}
		return json.dumps(data, indent=4)
	def isfound(self):
		data = super().get(f"link = '{self.link}'")
		return bool(len(data))

class ChannelDB(db):
	def __init__(self):
		super().__init__('channel',"(?,?,?)")
	def get(self , condition = ""):
		data = super().get(condition)
		items = []
		for i in data:
			items.append(channel(i[0],i[1],i[2]))
		return items
	def insert(self, values = ("name","link","thumbnail")):
		super().insert(values)
	def delete(self,value):
		super().delete(name="link",value=value)
	def updated(self,tup):
		super().updated(new=f"name = '{tup[0]}' ,thumbnail='{tup[2]}'" , old= f"link = '{tup[1]}'")

class channel(ChannelDB):
	def __init__(self,name,link,thumbnail):
		self.tup = (name,link,thumbnail)
		self.name = self.tup[0]
		self.link = self.tup[1]
		self.thumbnail = self.tup[2]
		super().__init__()
	def insert(self):
		super().insert(self.tup)
	def delete(self):
		super().delete(self.link)
	def updated(self, name= None ,thumbnail =None):
		if name  is None: name = self.name
		if thumbnail  is None: thumbnail = self.thumbnail
		self.tup = (name,self.link,thumbnail)
		self.name = self.tup[0]
		self.link = self.tup[1]
		self.thumbnail = self.tup[2]
		super().updated(self.tup)
	def __str__(self) :
		data = {
			'type': 'channel',
			'name': self.name,
			'link': self.link,
			'thumbnail': self.thumbnail,
		}
		return json.dumps(data, indent=4)
	def isfound(self):
		data = super().get(f"link = '{self.link}'")
		return bool(len(data))

def getallData():
		data = {
		'video': VideoDB().get(),
		'channel': 	ChannelDB().get(),
		'playlist': PlaylistDB().get(),
		"search" :	SearchDB().get()
	}
		return data
# c =video("","","","")
# x = dict(c.__dict__)
# print(c)
"""print(video("amr","daw","","")._db__name)
x = VideoDB()
x._db__name = ""
print(x._db__name)"""
"""
Example usage
video_db = VideoDB()
data = video_db.get()
print(data)
video_db.insert([('music', 'amr', 'asdsad'), ('music', 'amr', 'asdsad')])
data = video_db.get()
print(data)
video_db.delete("amr")
data = video_db.get()
print(data)
"""







"""v = video("python" , "fR_D_KIAYrE" , "")
print(v.get())
v.insert()
print(v.get())
v.updated(v.tup[0],"c:")
print(v.get())
v.delete()
print(v.get())"""










"""s = search("python")
print(s.get())
s.insert()
print(s.get())
s.updated("music")
print(s.get())
s.delete()
print(s.get())"""