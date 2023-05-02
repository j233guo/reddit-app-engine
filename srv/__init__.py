from flask import Flask
from credentials import credentials
from . import NetworkAPI

client_id = credentials.get('client_id')
secret = credentials.get('secret')
username = credentials.get('username')
password = credentials.get('password')

api = NetworkAPI.NetworkAPI(client_id=client_id, secret=secret, username=username, password=password)

def create_app():
    app = Flask(__name__)
    if api.get_access_token() == False:
        raise RuntimeError("Failed to obtain access token.")
    
    from .contents import contents as contents_blueprint
    app.register_blueprint(contents_blueprint)

    from .account import account as account_blueprint
    app.register_blueprint(account_blueprint)

    from .utils import utils as utils_blueprint
    app.register_blueprint(utils_blueprint)
    
    return app