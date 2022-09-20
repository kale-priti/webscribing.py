import json
from Task_1 import movie
def Top_movie():
    b=[]
    for i in movie:
        b.append(i["year"])
    b.sort()
    print(b)
    new={}
    for i in b:
        k=[]
        for j in movie:
            if j["year"]==i:
                k.append(j)
        new.update({i:k})
    with open("Task_2.json","w")as f:
        g=json.dump(new,f,indent=4)
Top_movie()





