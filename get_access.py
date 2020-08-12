import requests
import json
from collections import Counter

host = "http://127.0.0.1:8000"
token_url = "{host}/auth/accesstoken/?api".format(host=host)
print(token_url)
app_info = {
    "appname": "test_app",
    "client_id": "WhzraLaqVzRSyAJQ",
    "client_secret": "SQ7kIkxINl1ybWqW"
}


session = requests.session()
response = session.post(token_url,app_info)
token = json.loads(response._content)
print(token)