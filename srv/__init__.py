import requests
from flask import Flask

from credentials import credentials

def create_app():
    app = Flask(__name__)
    client_id = credentials.get('CLIENT_ID')
    secret = credentials.get('SECRET')
    username = credentials.get('USERNAME')
    password = credentials.get('PASSWORD')
    headers = {'User-Agent': 'python:app-engine:v0.0.1 (by /u/anonymousaudience)'}
    data = {'grant_type': 'password', 'username': username, 'password': password}
    auth = requests.auth.HTTPBasicAuth(client_id, secret)
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                auth=auth, data=data, headers=headers)
    TOKEN = res.json()['access_token']
    print(TOKEN)
    return app