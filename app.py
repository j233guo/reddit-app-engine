import os

from flask import jsonify, make_response, send_from_directory
from flask_cors import cross_origin

from srv import create_app
from srv.NetworkAPI import NetworkAPI

app = create_app()


@app.route('/home', defaults={'path': ''})
@app.route('/<path:path>')
@cross_origin()
def serve_frontend(path):
    print(app.static_folder)
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')
    

@app.route('/', methods=['GET'])
@cross_origin()
def root():
    access_token = NetworkAPI.check_access_token()
    if access_token:
        return jsonify({'message': 'Hello, World! The app is up and running. Please make POST requests listed in the README.'})
    else:   
        return jsonify({'message': 'Hello, World! The app is on but it\'s not ready to take requests because it\'s missing Reddit access token.'})


@app.errorhandler(404)
@cross_origin()
def endpoint_not_found(_error):
    return make_response(jsonify({'message': 'invalid url', 'code': -2}), 404)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='127.0.0.1', port=port)
