import json

dict={
    1:10,
    2:20,
    3:30,
    4:40,
    5:50
}

string=json.dumps(dict)
print(string)