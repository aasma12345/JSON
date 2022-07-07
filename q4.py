import json
# a={12:3}
# string=json.dumps(a)
# print(string)


# Q.1 Json data ko python object main convert karne ka program likho?.
# import json


dict='{"a":10,"b":20,"c":30,"d":40}'
convert=json.loads(dict)
print(convert)
print(convert["a"])
print(convert["b"])

