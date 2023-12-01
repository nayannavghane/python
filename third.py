# write a program in python,to open a browser window and open "youtube.com" and output the name of first video.
from selenium import webdriver
import selenium
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/watch?v=UDpo7StAvpw&t=658s")
print("success!")
