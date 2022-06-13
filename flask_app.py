from flask import Flask
from flask_cors import CORS
from flask import request, g
import time


def create_app():
    app = Flask(__name__)

    @app.before_request
    def before_request():
        g.start = time.time()

    @app.after_request
    def after_request(response):
        endpoint = request.endpoint
        diff = time.time() - g.start
        status = response.status_code
        args = request.args
        msg = "{} returned status: {} in time: {}\n{}".format(endpoint, status, diff, args)
        app.logger.info(msg)
        return response

    CORS(app)

    return app
