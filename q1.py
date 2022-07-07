import json
dict1={
    1:10,
    2:20,
    3:30
}
string=json.dumps(dict1)
print(string)
print(type(string))
