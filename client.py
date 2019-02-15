import requests
import json

r = requests.get('http://127.0.0.1:8000/one',)
print("Code: %s\nText: %s" % (r.status_code, r.text))

r = requests.get('http://127.0.0.1:8000/two',)
print("Code: %s\nText: %s" % (r.status_code, r.text))

r = requests.get('http://127.0.0.1:8000/notes',)
print("Code: %s\nText: %s" % (r.status_code, r.text))

payload = {
    'title': 'Note 2',
    'description': 'This is the description of Note 2',
    'priority': 1
}
r = requests.post('http://127.0.0.1:8000/notes', data=json.dumps(payload),
                  headers={'content-type': 'application/json'})
