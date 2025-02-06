import os

from flask import jsonify, make_response, send_from_directory
from flask_cors import cross_origin

from srv import create_app

app = create_app()

@app.route('/<path:path>')
@cross_origin()
def serve_frontend(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'main-page.html')
    

@app.route('/', methods=['GET'])
@cross_origin()
def main_page():
    try:
        return send_from_directory(app.static_folder, 'main-page.html')
    except Exception:
        return send_from_directory(app.static_folder, 'page-unavailable.html')

@app.route('/home', methods=['GET'])
@cross_origin()
def frontend_page():
    try:
        return send_from_directory(app.static_folder, 'index.html')
    except Exception:
        return send_from_directory(app.static_folder, 'page-unavailable.html')


@app.errorhandler(404)
@cross_origin()
def endpoint_not_found(_error):
    return make_response(jsonify({'message': 'invalid url', 'code': -2}), 404)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("HOST", '127.0.0.1')
    app.run(host=host, port=port)
