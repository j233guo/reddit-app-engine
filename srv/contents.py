from flask import Blueprint, jsonify, make_response
from flask_cors import cross_origin

from . import api

contents = Blueprint('contents', __name__)

@contents.route('/r/<subreddit>/<option>', methods=["POST"])
@cross_origin()
def get_posts_from_subreddit(subreddit, option):
    try:
        res = api.get(url=f'r/{subreddit}/{option}')
        return make_response(jsonify(res["data"]["children"]), 200)
    except Exception as e:
        return make_response(jsonify({"message": "Encountered an error", "code": -1}), 200)