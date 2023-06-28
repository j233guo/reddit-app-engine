from flask import jsonify, make_response
from flask_cors import cross_origin

from srv import create_app

app = create_app()

@app.errorhandler(404)
@cross_origin()
def endpoint_not_found(error):
    return make_response(jsonify({ 'message': 'invalid url', 'code': -2 }, 200))

if __name__ == '__main__':
    app.run()
