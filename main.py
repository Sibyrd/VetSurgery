import json

x = '{{"name":"test", "type":2}}'

with open('db.json', 'w') as f:
    json.dump(x, f)