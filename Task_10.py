import json 
def t10():
    with open("Task_5_FULLMOVIE.json") as f:
        movie_data=json.load(f)
        lang=[]
        director=[]
        for i in movie_data:
            for k in i["language"]:
                if k not in lang:
                    lang.append(k)
            if i["director"] not in director:
                director.append(i["director"])
        print(len(director))
        dic={}
        for i in director:
            l={}
            for k in lang:
                c=0
                for j in movie_data:
                    for p in j["language"]:
                        if i==j["director"] and k==p:
                            c=c+1
                if c>=1:
                    l.update({k:c})
            dic.update({i:l})
        with open("Task_10.json","w") as f:
            p=json.dump(dic,f,indent=4)
t10()



