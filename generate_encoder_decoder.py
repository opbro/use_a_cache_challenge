from random import randint
from string import printable
import json


a = list(printable)
b = set()

for i in a:
    x = randint(1,10000)
    while x in b:
        x = randint(1,10000)
    b.add(x)

b = list(b)

encoder = {x:y for x,y in zip(a,b)}
decoder = {y:x for x,y in zip(a,b)}

with open('encoder.json', 'w') as _file:
    json.dump(encoder,_file)

with open('decoder.json', 'w') as _file:
    json.dump(decoder,_file)