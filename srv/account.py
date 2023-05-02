from flask import Blueprint, jsonify, make_response
from flask_cors import cross_origin

from . import api

account = Blueprint('account', __name__)

@account.route('/me', methods=["POST"])
@cross_origin()
def get_identity():
    try:
        res = api.get(url='/api/v1/me')
        return make_response(jsonify(res), 200)
    except Exception as e:
        return make_response(jsonify({"message": "Encountered an error", "code": -1}), 200)
    
@account.route('/prefs', methods=["POST"])
@cross_origin()
def get_prefs():
    try:
        res = api.get(url='/api/v1/me/prefs')
        return make_response(jsonify(res), 200)
    except Exception as e:
        return make_response(jsonify({"message": "Encountered an error", "code": -1}), 200)