from flask import Blueprint, jsonify, make_response
from flask_cors import cross_origin

from . import api

account = Blueprint('account', __name__)

@account.route('/me', methods=["POST"])
@cross_origin()
def get_identity():
    try:
        response = api.get(url='/api/v1/me')
        response["code"] = 0
        return make_response(jsonify(response), 200)
    except Exception as e:
        response = api.generateErrorResponse(str(e))
        return make_response(jsonify(response), 200)
    
@account.route('/prefs', methods=["POST"])
@cross_origin()
def get_prefs():
    try:
        response = api.get(url='/api/v1/me/prefs')
        response["code"] = 0
        return make_response(jsonify(response), 200)
    except Exception as e:
        response = api.generateErrorResponse(str(e))
        return make_response(jsonify(response), 200)