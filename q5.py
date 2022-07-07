import json

dict={
    "name": "David", 
    "class": "I", 
    "age": 6
}

f=open("data.json","w")
json.dump(dict,f,indent=5)
f.close()

