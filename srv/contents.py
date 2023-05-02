from flask import Blueprint, jsonify, make_response, request
from flask_cors import cross_origin

from . import api

contents = Blueprint('contents', __name__)

@contents.route('/list', methods=["POST"])
@cross_origin()
def get_post_list():
    try:
        params = request.get_json()
        res = api.get(url=f'r/{params["subreddit"]}/{params["option"]}')
        return make_response(jsonify(res["data"]["children"]), 200)
    except Exception as e:
        return make_response(jsonify({ "message": "Encountered an error", "code": -1 }), 200)
    
@contents.route('/post', methods=["POST"])
@cross_origin()
def get_post():
    try:
        params = request.get_json()
        res = api.get(url=f'{params["permalink"]}')
        return make_response(jsonify(res), 200)
    except Exception as e:
        return make_response(jsonify({ "message": "Encountered an error", "code": -1 }), 200)