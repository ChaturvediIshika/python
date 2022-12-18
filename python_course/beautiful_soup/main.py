from bs4 import BeautifulSoup
import requests

URL="https://www.filmfare.com/features/best-comedy-movies-to-binge-watch-49887-1.html"

response=requests.get(URL)
website_data=response.text
 
soup= BeautifulSoup(website_data,"html.parser")

all_movies=soup.find_all(name="h2",dir_="ltr")
movie_titles=[movie.getText() for movie in all_movies]
movies=movie_titles[::-1]

with open("movies.txt",mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")