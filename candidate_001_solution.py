import requests
import time

url = 'http://104.248.58.163:8200'

# Documentation:
# ------
#         challenge
#     route: /challenge
#     Example: http://104.248.58.163:8200/challenge
#     Response: 
# 7979,106,137,8013,115,8253,7622,3117,7622,5332,3117,115,9851,8253,1627,6236,106,137,5767,2120,9057,76...
# ------
#        GET
#     route /decode
#     params : value
#     response:
#         decoded value
#     Examples:
#         http://104.248.58.163:8200/decode?value=7979
#     Responses:
#         Y
#     Bad resquest:
#         http://104.248.58.163:8200/decode?value=novalue
#     bad response:
#         Value [novalue] doesn't exsist in decoder map
        
# Challenge:
#         Decode the response from challenge by using the comma delimited values 
#         Code needs to finish in less then a minute.
# Optional: 
#       Give me the top 5 characters in the document, and their percent distribution
#       and the top 3 words in the document, and their percent distribution


response = requests.get("http://104.248.58.163:8200/challenge")
response_arr = response.text.split(",")

decode_chars = {code:"" for code in set(response_arr)}

decode_arr = []
for code in response_arr:
    #if not decode, request decoding and add to dict
    if decode_chars[code] == "":
        decode_char = requests.get("http://104.248.58.163:8200/decode?value=" + code).text
        decode_chars[code] = decode_char 
    #otherwise just look it up
    else:
        decode_char = decode_chars[code]
    decode_arr.append(decode_char)

print(''.join(decode_arr))