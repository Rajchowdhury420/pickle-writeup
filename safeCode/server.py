import json

f = open('users.json', 'r')
data = json.load(f)

print(data)
