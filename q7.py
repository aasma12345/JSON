import json

dict={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}



f=open("sort.json","w")

sorted_json=json.dump(dict,f,sort_keys=True,indent=4)
f.close()


