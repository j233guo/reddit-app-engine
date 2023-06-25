from flask import Blueprint, jsonify, make_response, request
from flask_cors import cross_origin

from . import api

contents = Blueprint('contents', __name__)

@contents.route('/api/general/list', methods=["POST"])
@cross_origin()
def get_post_list():
    try:
        params = request.get_json()
        response = api.get(url=f'r/{params["subreddit"]}/{params["option"]}')
        response["code"] = 0
        return make_response(jsonify(response), 200)
    except Exception as e:
        response = api.generateErrorResponse(str(e))
        return make_response(jsonify(response), 200)
    
@contents.route('/api/general/post', methods=["POST"])
@cross_origin()
def get_post():
    try:
        params = request.get_json()
        response = api.get(url=f'{params["permalink"]}')
        response["code"] = 0
        return make_response(jsonify(response), 200)
    except Exception as e:
        response = api.generateErrorResponse(str(e))
        return make_response(jsonify(response), 200)