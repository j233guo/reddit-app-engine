from flask import Blueprint, jsonify, make_response
from flask_cors import cross_origin

from . import api

misc = Blueprint('misc', __name__)


@misc.route('/api/misc/check', methods=['POST'])
@cross_origin()
def check():
    try:
        if not api.check_access_token():
            return make_response({'message': 'Access token not available', 'code': -1}, 200)
        return make_response({'status': 'OK', 'code': 0}, 200)
    except Exception as e:
        return make_response(jsonify({'message': 'Encountered an error', 'code': -1}), 200)
