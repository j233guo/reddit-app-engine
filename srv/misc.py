from flask import Blueprint, jsonify, make_response, send_from_directory
from flask_cors import cross_origin

from . import api

misc = Blueprint('misc', __name__, static_folder='static')


@misc.route('/api/misc/check', methods=['POST'])
@cross_origin()
def check_access_token():
    try:
        if not api.check_access_token():
            return make_response({'message': 'Access token not available', 'code': -1}, 200)
        return make_response({'status': 'OK', 'code': 0}, 200)
    except Exception as e:
        return make_response(jsonify({'message': 'Encountered an error', 'code': -1}), 200)


@misc.route('/api/misc/check', methods=['GET'])
@cross_origin()
def check_access_token_page():
    try:
        if not api.check_access_token():
            return send_from_directory(misc.static_folder, 'no-access-token.html')
        return send_from_directory(misc.static_folder, 'access-token-ok.html')
    except Exception as e:
        return send_from_directory(misc.static_folder, 'error.html')
