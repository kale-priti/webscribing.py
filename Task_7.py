import json 
def t7():
    with open("Task_5.json") as f:
        k=json.load(f)
    list1=[]
    for i in k:
        if i not in list1:
            list1.append(i["director"])
    director={}
    for i in list1:
        c=0
        for j in k:
            if j["director"]==i:
                c=c+1
        director.update({i:c})
    with open("Task_7.json","w") as f:
        json.dump(director,f,indent=4)
t7()
                





# import json 
# def t7():
#     with open("Task_5_FULLMOVIE.json") as f:
#         k=json.load(f)
#     list1=[]
#     for i in k:
#         if i not in list1:
#             list1.append(i["director"])
#     director={}
#     for i in list1:
#         c=0
#         for j in k:
#             if j["director"]==i:
#                 c=c+1
#         director.update({i:c})
#     with open("Task_7_directore.json","w") as f:
        # json.dump(director,f,indent=4)
# t7()
               
