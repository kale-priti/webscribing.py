
import json 
import requests
from bs4 import BeautifulSoup
from Task_1 import movie

def t5():
    movie_data=[]
    for i in range(len(movie)):
        dic={}
        k=[]
        dic["name"]=movie[i]["movie_name"]
        a=movie[i]['link']
        # print(a)
        page=requests.get(a)
        soup=BeautifulSoup(page.text,"html.parser")
        director=soup.find("a",class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link").get_text()
        dic["director"]=director
        poster_image=soup.find("div",class_="ipc-media ipc-media--poster-27x40 ipc-image-media-ratio--poster-27x40 ipc-media--baseAlt ipc-media--poster-l ipc-poster__poster-image ipc-media__img").img['src']
        dic["postername"]=poster_image
        bio=soup.find("span",class_="sc-16ede01-2 gXUyNh").get_text()
        dic["bio"]=[bio]
        abc=soup.find('div',class_="ipc-chip-list__scroller")
        genre=abc.find_all('span')
        list1=[]
        for i in genre:
            list1.append(i.get_text())
        dic['genre']=list1
        Detail=soup.find("section",cel_widget_id="StaticFeature_Details")
        s=Detail.find_all("div")
        y=[]
        for ul in s:
            h=ul.find_all("ul")
            for li in h:
                o=li.find_all("li")
                for aa in o:
                    z=aa.find_all('a')
                    d=[]
                    for i in z:
                        k=i.get_text()
                        d.append(k)
                    for i in d:
                        if i not in y:
                            y.append(i)
        list1=["Bangla", " Bengali","English","Bodo", "Dogri", "Gujarati", "Hindi", "Kashmiri", "Kannada", "Konkani", "Maithili", "Malayalam", "Manipuri", "Marathi", "Nepali", "Oriya", "Punjabi", "Tamil", "Telugu", "Santali", "Sindhi", "Urdu","Assamese" ]
        lang=[]
        for i in y:
            for j in list1:
                if i==j:
                    lang.append(i)
        dic["language"]=lang
        b=y[1].split()
        dic["release_year"]=b[2]
        # dic["country"]=b[3]
        dic["release_date"]=b[1]+b[0]
        movie_data.append(dic)
    with open("Task_5_FULLMOVIE.json","w")as f:
        json.dump(movie_data,f,indent=4)
    return movie_data
t5()
