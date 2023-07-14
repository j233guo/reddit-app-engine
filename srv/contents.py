from flask import Blueprint, jsonify, make_response, request
from flask_cors import cross_origin

from . import api
from .models import Post, Comment

contents = Blueprint('contents', __name__)

@contents.route('/api/general/posts', methods=['POST'])
@cross_origin()
def get_posts():
    try:
        reqjson = request.get_json()
        url = f"r/{reqjson['subreddit']}/{reqjson['listingOption']}"
        params = {
            "limit": reqjson.get('limit'),
            "before": reqjson.get('before'),
            "after": reqjson.get('after')
        }
        data = api.get(url=url, params=params)
        posts = []
        for item in data['data']['children']:
            post = Post(
                id = item['data'].get('id'),
                author = item['data'].get('author', '[deleted]'),
                created_utc = item['data'].get('created_utc', '0'),
                media = item['data'].get('media'),
                name = item['data'].get('name'),
                num_comments = item['data'].get('num_comments'),
                permalink = item['data'].get('permalink'),
                preview = item['data'].get('preview'),
                score = item['data'].get('score'),
                selftext = item['data'].get('selftext', ''),
                selftext_html = item['data'].get('selftext_html', ''),
                subreddit = item['data'].get('subreddit'),
                thumbnail = item['data'].get('thumbnail'),
                title = item['data'].get('title'),
                url = item['data'].get('url')
            )
            posts.append(post)
        return make_response(jsonify({ 'posts': posts, 'code': 0 }), 200)
    except Exception as e:
        response = api.generateErrorResponse(str(e))
        return make_response(jsonify(response), 200)
    
@contents.route('/api/general/comments', methods=['POST'])
@cross_origin()
def get_comments():
    try:
        reqjson = request.get_json()
        url = f"r/{reqjson['subreddit']}/comments/{reqjson['id']}"
        params = {
            "limit": reqjson.get('limit'),
            "depth": reqjson.get('depth')
        }
        response = api.get(url=url, params=params)
        comment_list = response[1]
        comments = []
        for item in comment_list['data']['children'][:-1]:
            comment = Comment(
                id = item['data'].get('id'),
                author = item['data'].get('author', '[deleted]'),
                body = item['data'].get('body', '[deleted]'),
                body_html = item['data'].get('body_html'),
                created_utc = item['data'].get('created_utc', '0'),
                name = item['data'].get('name'),
                permalink = item['data'].get('permalink'),
                score = item['data'].get('score')
            )
            comments.append(comment)
        return make_response(jsonify({ 'comments': comments, 'code': 0 }), 200)
    except Exception as e:
        response = api.generateErrorResponse(str(e))
        return make_response(jsonify(response), 200)