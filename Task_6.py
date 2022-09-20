import json
def t6():
    with open("Task_5.json") as f:
        k=json.load(f)
        lang=[]
        for i in k:
            for j in i["language"]:
                if j not in lang:
                    lang.append(j)
        # print(lang)
        lang_data={}
        for i in lang:
            c=0
            for l in k:
                for j in l["language"]:
                    if j==i:
                        c+=1
            lang_data.update({i:c})
        with open("Task_6_FULL_language.json","w") as f:
            k=json.dump(lang_data,f,indent=4)
t6()