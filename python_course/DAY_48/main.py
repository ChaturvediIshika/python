from selenium import webdriver

chrome_server_path="C:\DEVELOPMENT\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_server_path)

driver.get("https://www.python.org/")
dates=driver.find_elements_by_css_selector('.event-widget time')
t=[date.text for date in dates]

names=driver.find_elements_by_css_selector('.event-widget li a')
n=[name.text for name in names]

d={}
for i in range(0,5):
    d[i]={
        "time":t[i],
        "name":n[i]
    }
print(d)
driver.quit()