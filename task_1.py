import json
from bs4 import BeautifulSoup
import requests
url='https://www.imdb.com/india/top-rated-indian-movies//'
page=requests.get(url)
soup=BeautifulSoup(page.text,'html.parser')
def top_movies():
    main_div=soup.find('div',class_='lister')
    tbody=main_div.find('tbody',class_='lister-list')
    trs=tbody.find_all('tr')
    movie_rank=[]
    movie_name=[]
    release_year=[]
    movie_rating=[]
    movie_link=[]
    for tr in trs:
        positation=tr.find('td',class_="titleColumn").get_text().strip()
        rank=""
        for i in positation:
            if '.' not in i:
                rank+=i
            else:
                break
        movie_rank.append(rank)
        title=tr.find('td',class_='titleColumn').a.get_text()
        movie_name.append(title)
        year=tr.find('td',class_='titleColumn').span.get_text()
        release_year.append(year)
        reating=tr.find('td',class_="ratingColumn imdbRating").strong.get_text()
        movie_rating.append(reating)
        link=tr.find('td',class_='titleColumn').a['href']
        mo_link="https://www.imdb.com"+link
        movie_link.append(mo_link)
    movie=[]
    details={"movie_name":"","movie_rank":"","movie_rating":"", "release_year":",","link":""}
    for i in range (0,len(movie_rank)):
        details["movie_name"]=str(movie_name[i])
        details["movie_rank"]=movie_rank[i]
        details["movie_rating"]=float(movie_rating[i])
        release_year[i]=release_year[i][1:5]
        details["release_year"]=int(release_year[i])
        details["link"]=movie_link[i]
        movie.append(details.copy())
    with open("movies_data.json","w")as f:
        g=json.dump(Top_movie,f,indent=4)
top_movies()
