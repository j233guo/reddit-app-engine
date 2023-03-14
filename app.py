from flask import Flask, abort, jsonify, make_response, request
from flask_cors import CORS, cross_origin

from credentials import credentials
from srv.NetworkAPI import NetworkAPI

api = NetworkAPI()
app = Flask(__name__)
cors = CORS(app)
app.abort = abort
app.request = request

client_id = credentials.get('client_id')
secret = credentials.get('secret')
username = credentials.get('username')
password = credentials.get('password')

@app.route('/<method>', methods=['POST'])
@cross_origin()
def get_task(method):
    try:
        if (api.check_access_token() == False):
            try:
                api.get_access_token(client_id=client_id, secret=secret, username=username, password=password)
            except Exception as e:
                return make_response(jsonify({"message": f"Encountered error: {e}", "code": -1}), 200)
        res = api.get(url=method)
        return make_response(jsonify(res), 200)
    except Exception as e:
        print(e)
        return make_response(jsonify({"message": "Encountered an error", "code": -1}), 200)

if __name__ == '__main__':
    app.run()
