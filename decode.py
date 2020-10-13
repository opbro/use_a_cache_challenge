import json
import sys

textfile = sys.argv[1]

with open(textfile) as _file:
    data = _file.read().split(',')

with open('decoder.json') as _file:
    decoder = json.load(_file)

decoded = ''
for i in data:
    decoded += decoder[i]

print(decoded)

letter_dist = dict()
word_dist = dict()
for i in decoded:
    letter_dist.setdefault(i, 0)
    letter_dist[i] += 1

for i in decoded.split(' '):
    word_dist.setdefault(i,0)
    word_dist[i] += 1

print(json.dumps(letter_dist, indent=4))
print(json.dumps(word_dist, indent=4))