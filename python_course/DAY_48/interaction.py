from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_server_path="C:\DEVELOPMENT\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_server_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

name=driver.find_element_by_name("fName")
name.send_keys("Ishika")

last=driver.find_element_by_name("lName")
last.send_keys("Chaturvedi")

email=driver.find_element_by_name("email")
email.send_keys("ishikachaturvedi322@gmail.com")

search=driver.find_element_by_css_selector("form button")
search.click()
