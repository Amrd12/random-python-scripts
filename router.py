from selenium import webdriver
import time
bro = webdriver.Edge()
bro.get("http://192.168.1.1/")
user = bro.find_elements("name", "Username")[0]
pas = bro.find_elements("name", "Password")[0]
sub = bro.find_element("id", "LoginId")


user.send_keys("admin")
pas.send_keys("amr12alnbawy")
sub.click()
time.sleep(30)