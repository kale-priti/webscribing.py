

from task_1 import top_movies
import json
import os
url=movie[1]["link"]
def movie_details(movie_detail):
    movie_id=""
    for i in movie_detail[27:-1]:
        movie_id+=i
    filename=movie_id+".json"
    text=os.path.exists(filename)
    if text==True:
        with open(filename,"r")as f:
            a=json.load(f)
        print(a)
    else:
        with open("Task_4.json")as f:
            data=json.load(f)
        with open(filename,"w") as f:
            json.dump(data,f,indent=4)
movie_details(url)
