import json 
def task():
    with open("Task_5_FULLMOVIE.json") as f:
        data=json.load(f)
        genre=[]
        for i in data:
            for j in i["genre"]:
                if j not in genre:
                    genre.append(j)
        # print(genre)
        dic={}
        for i in genre:
            c=0
            for j in data:
                for k in j["genre"]:
                    if i==k:
                        c=c+1
            if c>=1:
                dic.update({i:c})
        with open("Task_11.json","w") as f:
            k=json.dump(dic,f,indent=4)

task()