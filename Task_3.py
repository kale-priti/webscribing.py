from  Task_1 import movies_data
import json
def Top_movie():
    b=[]
    for i in movie:
        b.append(i["year"])
    b.sort()
    i=b[0]-5
    l1=b[-1]
    new={}
    while i<l1:
        list1=[]
        for j in movie:
            if j["year"]>=i and j["year"]<=i+10 :
                list1.append(j)
        new.update({i:list1})
        i=i+10
    with open("Task_3.json","w") as f:
        l=json.dump(new, f,indent=4)
Top_movie()
