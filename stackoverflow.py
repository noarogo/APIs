import requests
import json

response = requests.get('http://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

# print(response.json()['items'])

for q in response.json()['items']:
    if q['answer_count'] == 0:
        print(q['title'])
        print(q['link'])
    else:
        print("skipped")
    print()