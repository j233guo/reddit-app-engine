from flask import Flask
from . import NetworkAPI
from dotenv import load_dotenv

import os

load_dotenv()

required_credentials = [
    'REDDIT_API_CLIENT_ID',
    'REDDIT_API_SECRET',
    'REDDIT_API_USERNAME',
    'REDDIT_API_PASSWORD'
]
    
missing_credentials = [var for var in required_credentials if not os.environ.get(var)]
if missing_credentials:
    raise EnvironmentError(
        f"Missing required environment variables: {', '.join(missing_credentials)}\n"
        "Check your .env file or deployment environment configuration."
    )

client_id = os.environ.get('REDDIT_API_CLIENT_ID')
secret = os.environ.get('REDDIT_API_SECRET')
username = os.environ.get('REDDIT_API_USERNAME')
password = os.environ.get('REDDIT_API_PASSWORD')

api = NetworkAPI.NetworkAPI(client_id=client_id, secret=secret, username=username, password=password)

def create_app():
    app = Flask(__name__, static_folder='webapp')

    if not api.get_access_token():
        raise RuntimeError('Failed to obtain access token.')

    from .contents import contents as contents_blueprint
    app.register_blueprint(contents_blueprint)

    from .account import account as account_blueprint
    app.register_blueprint(account_blueprint)

    from .misc import misc as misc_blueprint
    app.register_blueprint(misc_blueprint)

    return app
