import os
import traceback
from flask_app import create_app
from werkzeug.middleware.proxy_fix import ProxyFix

try:
    APP = create_app()
    APP.wsgi_app = ProxyFix(APP.wsgi_app)
    from data_app.api import register_api
    register_api(APP)

except Exception as e:
    trace = traceback.format_exc()
    APP.logger.error("unable to start API: {}\n{}".format(e, trace))
    exit(1)

if __name__ == '__main__':
    PORT = int(os.getenv('PORT', 8000))
    APP.logger.info(f"APP running on port: {PORT}")
    APP.run(port=PORT, debug=True)
