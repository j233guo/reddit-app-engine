from flask import Blueprint, jsonify, make_response, request
from flask_cors import cross_origin

from . import api
from .models import Post, Comment

contents = Blueprint('contents', __name__)

@contents.route('/api/general/listing', methods=['POST'])
@cross_origin()
def get_post_list():
    try:
        params = request.get_json()
        data = api.get_listing(url=f"r/{params['subreddit']}/{params['listingOption']}", limit=params['limit'])
        posts = []
        for item in data['data']['children']:
            post = Post(
                id = item['data'].get('id'),
                author = item['data'].get('author', '[deleted]'),
                created_utc = item['data'].get('created_utc', '0'),
                media = item['data'].get('media'),
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
    
@contents.route('/api/general/post', methods=['POST'])
@cross_origin()
def get_post():
    try:
        params = request.get_json()
        response = api.get(url=params['permalink'])
        post_data = response[0]
        comment_list = response[1]
        comments = []
        parsed_post_data = post_data['data']['children'][0]
        post = Post(
            id = parsed_post_data['data'].get('id'),
            author = parsed_post_data['data'].get('author', '[deleted]'),
            created_utc = parsed_post_data['data'].get('created_utc', '0'),
            media = parsed_post_data['data'].get('media'),
            num_comments = parsed_post_data['data'].get('num_comments'),
            permalink = parsed_post_data['data'].get('permalink'),
            preview = parsed_post_data['data'].get('preview'),
            score = parsed_post_data['data'].get('score'),
            selftext = parsed_post_data['data'].get('selftext', ''),
            selftext_html = parsed_post_data['data'].get('selftext_html', ''),
            subreddit = parsed_post_data['data'].get('subreddit'),
            thumbnail = parsed_post_data['data'].get('thumbnail'),
            title = parsed_post_data['data'].get('title'),
            url = parsed_post_data['data'].get('url')
        )
        for item in comment_list['data']['children']:
            comment = Comment(
                id = item['data'].get('id'),
                author = item['data'].get('author', '[deleted]'),
                body = item['data'].get('body'),
                body_html = item['data'].get('body_html'),
                created_utc = item['data'].get('created_utc', '0'),
                permalink = item['data'].get('permalink'),
                score = item['data'].get('score')
            )
            comments.append(comment)
        return make_response(jsonify({ 'post': post, 'comments': comments, 'code': 0 }), 200)
    except Exception as e:
        response = api.generateErrorResponse(str(e))
        return make_response(jsonify(response), 200)