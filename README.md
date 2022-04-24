# notes.io-api
Restful API for notes.io

### Create Note
**Using Python**
```python
import requests
import json

url = "localhost:8000/api/v1/notes/"

payload = json.dumps({
    "title": "Note 1",
    "text": "Some text about Note 1"
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

```
![screenshot](screenshots/create_note.png)