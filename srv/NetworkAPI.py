import requests

class NetworkAPI:
    def __init__(self):
        self._base_url = "https://oauth.reddit.com/api/v1/"
        self._headers = {'User-Agent': 'python:app-engine:v0.0.1 (by /u/anonymousaudience)'}
        self._data = None
        self._auth = None
        self._access_token = None

    def check_access_token(self):
        return self._access_token != None

    def get_access_token(self, client_id, secret, username, password):
        self._auth = requests.auth.HTTPBasicAuth(client_id, secret)
        self._data = {'grant_type': 'password', 'username': username, 'password': password}
        res = requests.post('https://www.reddit.com/api/v1/access_token',
                auth=self._auth, data=self._data, headers=self._headers)
        if res.status_code != 200:
            raise Exception(res.status_code)
        self._access_token = res.json()['access_token']
        self._headers = {**self._headers, **{'Authorization': f"bearer {self._access_token}"}}

    def get(self, url):
        res = requests.get(self._base_url + url, headers=self._headers)
        if res.status_code != 200:
            raise Exception(res.status_code)
        return res.json()