import os

from flask import jsonify, make_response, send_from_directory
from flask_cors import cross_origin

from srv import create_app

app = create_app()


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
@cross_origin()
def serve(path):
    print(app.static_folder)
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


@app.errorhandler(404)
@cross_origin()
def endpoint_not_found(_error):
    return make_response(jsonify({'message': 'invalid url', 'code': -2}), 404)


if __name__ == '__main__':
    app.run()
