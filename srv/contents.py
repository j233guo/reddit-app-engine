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

        def build_reply_tree(reply_data):
            self_reply = Comment(
                id=reply_data.get('id'),
                author=reply_data.get('author', '[deleted]'),
                body=reply_data.get('body', '[deleted]'),
                body_html=reply_data.get('body_html'),
                created_utc=reply_data.get('created_utc', '0'),
                name=reply_data.get('name'),
                permalink=reply_data.get('permalink'),
                score=reply_data.get('score'),
                replies=[]
            )
            # Recursively process nested replies
            if type(reply_data.get('replies', None)) != str:
                child_replies = []
                for child in reply_data.get('replies', {}).get('data', {}).get('children', []):
                    if child['kind'] == 't1':
                        replies.append(build_reply_tree(child['data']))
                self_reply.replies = child_replies
            return self_reply

        comments = []
        for item in comment_list['data']['children'][:-1]:
            data = item['data']
            comment = Comment(
                id=data.get('id'),
                author=data.get('author', '[deleted]'),
                body=data.get('body', '[deleted]'),
                body_html=data.get('body_html'),
                created_utc=data.get('created_utc', '0'),
                name=data.get('name'),
                permalink=data.get('permalink'),
                score=data.get('score'),
                replies=[]
            )
            # Build reply tree for top-level comment
            if type(data.get('replies', None)) != str:
                replies = []
                for reply in data.get('replies', {}).get('data', {}).get('children', []):
                    if reply['kind'] == 't1':
                        replies.append(build_reply_tree(reply['data']))
                comment.replies = replies
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
