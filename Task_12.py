
import json
import requests
from bs4 import BeautifulSoup
url="https://www.imdb.com/title/tt4679210/"
page=requests.get(url)
soup=BeautifulSoup(page.text,"html.parser")
k=soup.find_all("cast_list")
print(k)