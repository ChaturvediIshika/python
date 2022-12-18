from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_server_path="C:\DEVELOPMENT\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_server_path)

driver.get("https://www.instagram.com/")

name=driver.find_element_by_css_selector("input[name='username']")
name.send_keys("__sanjana1234__")

password=driver.find_element_by_css_selector("input[name='password']")
password.send_keys("cishika104")

password.send_keys(Keys.ENTER)