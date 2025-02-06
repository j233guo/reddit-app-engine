# Reddit App Engine

A lightweight python web server that fetches Reddit API and serves [JG Reddit App web app](https://github.com/j233guo/jg-reddit-a).

This app is created in compliance with, and all usages should comply with, [Reddit API rules](https://github.com/reddit-archive/reddit/wiki/API).

[Live Version](https://reddit-app-engine.onrender.com)

## Before Starting

This app requires Reddit developer account credentials.

To obtain your own credentials, log into Reddit and go to [Reddit Preferences Page](https://www.reddit.com/prefs/apps/) where you can find the app tab. Click "create another app", and in the form, select "script", fill in the required fields, and click "create app". 
Once the app is created, you can find the client id below the app name, and secret key in the "edit" tab.

## Setup

Clone this repo and install the required dependencies with ```pip install -r requirements.txt```. 

The Reddit credentials are supplied with an env file. To create the env file, copy ```env.template``` as template and fill in the values with your own reddit app credentials.

## Usage as Local Server

Option 1: Start the app with ```python app.py```. 

OR

Option 2: Create a new file ```app.spec``` by copying the content of ```app.spec.template``` then build with ```pyinstaller app.spec```. Start the app by running the built executable in dist folder.

## Required Dependencies
* flask
* flask-cors
* requests
* python-dotenv

## API
| Method | Endpoint                               | Description                                             | Parameters                           | Optional                               |
|--------|----------------------------------------|---------------------------------------------------------|--------------------------------------|----------------------------------------|
| GET    | ```/```                                | Main page                                               | -                                    | -                                      |
| GET    | ```/home```                            | Frontend app                                            | -                                    | -                                      |
| POST   | ```/api/misc/check```                  | Check if server is working and access token is obtained | -                                    | -                                      |
| POST   | ```/api/account/me```                  | Get user info                                           | -                                    | -                                      |
| POST   | ```/api/account/prefs```               | Get user preferences                                    | -                                    | -                                      |
| POST   | ```/api/general/posts```               | Get a list of posts from a subreddit                    | ```subreddit```, ```listingOption``` | ```before```, ```after```, ```limit``` |
| POST   | ```/api/general/comments```            | Get the comments or replies of a post                   | ```subreddit```, ```id```            | ```depth```, ```limit```               |
| POST   | ```/api/general/search_reddit_names``` | Search subreddit names that begin with a query string   | ```include_over_18```, ```query```   | ```limit```                            |
