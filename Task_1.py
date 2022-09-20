
import json
from bs4 import BeautifulSoup
import requests
url='https://www.imdb.com/india/top-rated-indian-movies//'
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
t=soup.find('tbody',class_='lister-list')
b=t.find_all('tr')
movie=[]
for i in b:
    movie_details={}
    movie_name=i.find("td",class_="titleColumn").a.get_text()
    movie_details["movie_name"]=movie_name
    movie_rank=i.find("td",class_="titleColumn").get_text().strip().replace("\n","").replace(" ","")
    movie_rank=movie_rank[:1]
    movie_details["movie_rank"]=movie_rank
    rating=i.find("td",class_="ratingColumn imdbRating").strong.get_text()
    movie_details["movie_rating"]=float(rating)
    rating=i.find("td",class_="ratingColumn imdbRating").strong.get_text()
    movie_details["movie_rating"]=float(rating)
    year_of_release=i.find('td',class_="titleColumn").span.get_text()
    year=year_of_release[1:-1]
    movie_details["year"]=int(year)
    movie_link=i.find('td',class_="titleColumn").a["href"]
    link='https://www.imdb.com'+movie_link
    movie_details["link"]=link
    movie.append(movie_details)
    with open("Top_movie1.json","w")as f:
        g=json.dump(movie,f,indent=4)