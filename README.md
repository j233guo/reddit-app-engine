# Reddit App Engine

A lightweight python web server that fetches Reddit API and serves [JG Reddit App web app](https://github.com/j233guo/jg-reddit-a).

Created in compliance with [Reddit API rules](https://github.com/reddit-archive/reddit/wiki/API).

## Setup
Clone this repo and install the required dependencies with ```pip install -r requirements.txt```. 

***
This app requires Reddit developer account credentials supplied with an env file.
To create the env file, copy ```env.template``` as template and fill in the values.
To obtain your own credentials, create a Reddit developer account and create an app [here](https://www.reddit.com/prefs/apps/).
***

## Usage as Server

Option 1: Start the app with ```python app.py```. 

OR

Option 2: Create a new file ```app.spec``` by copying the content of ```app.spec.template``` then build with ```pyinstaller app.spec```. Start the app by running the built executable in dist folder.

Make POST requests.

## To Serve the Frontend Webapp
[Frontend Source Code](https://github.com/j233guo/jg-reddit-a)
Build the frontend with ```npm run build``` and place the built files in /srv/webapp. Start the app and go to the root URL from your browser. 

## Required Dependencies
* flask
* flask-cors
* requests
* python-dotenv

## API
| Endpoint                               | Description                                             | Parameters                           | Optional                               |
|----------------------------------------|---------------------------------------------------------|--------------------------------------|----------------------------------------|
| ```/api/misc/check```                  | Check if server is working and access token is obtained | -                                    | -                                      |
| ```/api/account/me```                  | Get user info                                           | -                                    | -                                      |
| ```/api/account/prefs```               | Get user preferences                                    | -                                    | -                                      |
| ```/api/general/posts```               | Get a list of posts from a subreddit                    | ```subreddit```, ```listingOption``` | ```before```, ```after```, ```limit``` |
| ```/api/general/comments```            | Get the comments or replies of a post                   | ```subreddit```, ```id```            | ```depth```, ```limit```               |
| ```/api/general/search_reddit_names``` | Search subreddit names that begin with a query string   | ```include_over_18```, ```query```   | ```limit```                            |
