from flask import Blueprint, jsonify, make_response, request
from flask_cors import cross_origin

from . import api

contents = Blueprint('contents', __name__)

@contents.route('/api/general/listing', methods=["POST"])
@cross_origin()
def get_post_list():
    try:
        params = request.get_json()
        response = api.get_listing(url=f'r/{params["subreddit"]}/{params["listingOption"]}', limit=params["limit"])
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