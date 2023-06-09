# Reddit App Engine

A lightweight python web server that fetches Reddit API. 

Created in compliance with [Reddit API rules](https://github.com/reddit-archive/reddit/wiki/API).

## Setup
Clone this repo and install the required dependencies with ```pip install -r requirements.txt```. 

***This app requires Reddit developer account credentials supplied with a module named ```credentials.py```.
It is excluded from this repository for obvious security reasons, but can be created with ```credentials.txt``` as template.***

## Usage
Start the app with ```python app.py```. Make http requests to the server. 
All requests are made in POST method.

Check [official Reddit API](https://www.reddit.com/dev/api/) for API path names.

## Required Dependencies
* flask
* flask-cors
* requests

## API
| Endpoint | Description | Parameters |
| --- | --- | --- |
| ```/check``` | Check if server is working and access token is obtained | none |
| ```/me``` | Get user info | none |
| ```/prefs``` | Get user preferences | none |
| ```/list``` | Get post list from a subreddit | ```subreddit```, ```option```|
| ```/post``` | Get a post or comment | ```permalink```| 
