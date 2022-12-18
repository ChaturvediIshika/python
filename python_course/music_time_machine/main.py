from bs4 import BeautifulSoup
import requests

date=input("Which year do you want to travel to? write date in  YYY-MM-DD format ")

URL=f"https://www.billboard.com/charts/hot-100/{date}"

response=requests.get(URL)
website_data=response.text

soup= BeautifulSoup(website_data,"html.parser")

all_songs=soup.find_all(name="span",class_="chart-element__information__song")

songs=[song.getText() for song in all_songs]

print(songs)