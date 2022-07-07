# import json


# dict='{"complex":"true", "real": 4, "img": 5}'
# string=json.loads(dict)
# print(string)

import json
def is_complex_num(objct):
    if 'complex' in objct:
        return complex(objct['real'], objct['img'])
    return objct

complex_object=json.loads('{"complex": true, "real": 4, "img": 5}',object_hook=is_complex_num)
simple_object=json.loads('{"real": 4, "img": 3}',object_hook=is_complex_num)
print(complex_object)
print(simple_object)

















