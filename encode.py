import sys
import json

textfile = sys.argv[1]

with open(textfile) as _file:
    data = _file.read()

with open('encoder.json') as _file:
    encoder = json.load(_file)

encoded = list()
for i in data:
    try:
        encoded.append(str(encoder[str(i)]))
    except:
        print(i, 'not mapping skipping')

encoded_text = ','.join(encoded)

with open('encoded.txt', 'w') as _file:
    _file.write(encoded_text)