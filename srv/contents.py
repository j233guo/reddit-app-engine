from flask import Blueprint, jsonify, make_response, request
from flask_cors import cross_origin

from . import api
from .models import Post, Comment

contents = Blueprint('contents', __name__)


@contents.route('/api/general/posts', methods=['POST'])
@cross_origin()
def get_posts():
    try:
        req_json = request.get_json()
        url = f"r/{req_json['subreddit']}/{req_json['listingOption']}"
        params = {
            "limit": req_json.get('limit'),
            "before": req_json.get('before'),
            "after": req_json.get('after')
        }
        data = api.get(url=url, params=params)
        posts = []
        for item in data['data']['children']:
            post = Post(
                id=item['data'].get('id'),
                author=item['data'].get('author', '[deleted]'),
                created_utc=item['data'].get('created_utc', '0'),
                media=item['data'].get('media'),
                media_metadata=item['data'].get('media_metadata'),
                name=item['data'].get('name'),
                num_comments=item['data'].get('num_comments'),
                permalink=item['data'].get('permalink'),
                preview=item['data'].get('preview'),
                score=item['data'].get('score'),
                selftext=item['data'].get('selftext', ''),
                selftext_html=item['data'].get('selftext_html', ''),
                subreddit=item['data'].get('subreddit'),
                thumbnail=item['data'].get('thumbnail'),
                title=item['data'].get('title'),
                url=item['data'].get('url')
            )
            posts.append(post)
        return make_response(jsonify({'posts': posts, 'code': 0}), 200)
    except Exception as e:
        response = api.generateErrorResponse(str(e))
        return make_response(jsonify(response), 200)


@contents.route('/api/general/comments', methods=['POST'])
@cross_origin()
def get_comments():
    try:
        req_json = request.get_json()
        url = f"r/{req_json['subreddit']}/comments/{req_json['id']}"
        params = {
            "limit": req_json.get('limit'),
            "depth": req_json.get('depth')
        }
        response = api.get(url=url, params=params)
        comment_list = response[1]
        comments = []
        for item in comment_list['data']['children'][:-1]:
            comment = Comment(
                id=item['data'].get('id'),
                author=item['data'].get('author', '[deleted]'),
                body=item['data'].get('body', '[deleted]'),
                body_html=item['data'].get('body_html'),
                created_utc=item['data'].get('created_utc', '0'),
                name=item['data'].get('name'),
                permalink=item['data'].get('permalink'),
                score=item['data'].get('score')
            )
            comments.append(comment)
        return make_response(jsonify({'comments': comments, 'code': 0}), 200)
    except Exception as e:
        response = api.generateErrorResponse(str(e))
        return make_response(jsonify(response), 200)


@contents.route('/api/general/search_reddit_names', methods=['POST'])
@cross_origin()
def search_reddit_names():
    try:
        req_json = request.get_json()
        params = {
            "include_over_18": req_json.get('include_over_18', True),
            "query": req_json.get('query'),
            "limit": req_json.get('limit'),
            "exact": False,
            "include_unadvertisable": True
        }
        response = api.get(url='/api/search_reddit_names', params=params)
        names = response.get('names')
        return make_response(jsonify({'names': names, 'code': 0}), 200)
    except Exception as e:
        response = api.generateErrorResponse(str(e))
        return make_response(jsonify(response), 200)
