import json
a=  {"name":"shikhu",
    "class":"I",
    "age": 4 
}
my_file=open("ques.json","w")
json.dump(a,my_file,indent=3)
my_file.close()


