import requests
import math

class NetworkAPI:
    def __init__(self, client_id, secret, username, password):
        self._base_url = "https://oauth.reddit.com/"
        self._headers = {'User-Agent': 'python:app-engine:v0.0.1 (by /u/anonymousaudience)'}
        self._data = None
        self._auth = None
        self._client_id = client_id
        self._secret = secret
        self._username = username
        self._password = password
        self._access_token = None

    def check_access_token(self):
        return self._access_token != None

    def get_access_token(self):
        self._auth = requests.auth.HTTPBasicAuth(self._client_id, self._secret)
        self._data = {'grant_type': 'password', 'username': self._username, 'password': self._password}
        res = requests.post('https://www.reddit.com/api/v1/access_token',
                auth=self._auth, data=self._data, headers=self._headers)
        if res.status_code != 200 or 'access_token' not in res.json():
            return False
        self._access_token = res.json()['access_token']
        self._headers = {**self._headers, **{'Authorization': f"bearer {self._access_token}"}}
        return True

    def get(self, url):
        res = requests.get(self._base_url + url, headers=self._headers)
        if res.status_code != 200:
            raise Exception(res.status_code)
        return res.json()
    
    def get_listing(self, url, limit=20):
        res = requests.get(self._base_url + url, headers=self._headers, params={ "limit": limit })
        if res.status_code != 200:
            raise Exception(res.status_code)
        return res.json()
    
    def generateErrorResponse(self, error_str):
        response = { "message": error_str }
        if str.isdigit(error_str) and len(error_str) == 3:
            response["code"] = -1
        else:
            response["code"] = -2
        return response