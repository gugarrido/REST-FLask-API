'''Initializing all the namespaces '''
from .restplus import DATABLUEPRINT, API
from .endpoints.backend.get_foo import ns as getfoo


def register_data(flask_app):
    API.add_namespace(getfoo)

    flask_app.register_blueprint(DATABLUEPRINT)


def register_api(flask_app):
    register_data(flask_app)
