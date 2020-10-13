import requests
import time

url = 'http://104.248.58.163:8200'

challenge = requests.get('{}/challenge'.format(url)).text.split(',')

cache = dict()

decoded = '' 
total_start = time.time()
print("Decoding {} letters".format(len(challenge)))
for i in challenge:
    start_time = time.time()
    if i not in cache:
        answer = requests.get('{}/decode'.format(url),params={'value':i}).text
        cache[i] = answer
    else:
        answer = cache[i]
    decoded += answer
    end_time = time.time()

print(decoded)
total_end = time.time()

print("Took a total of {} seconds".format(int(total_end - total_start)))