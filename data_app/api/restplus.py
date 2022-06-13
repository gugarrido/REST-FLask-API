from flask import Blueprint
from flask_restx import Api

#backend
url_prefix = "/data/api"
DATABLUEPRINT = Blueprint('API', __name__, url_prefix=url_prefix)
API = Api(DATABLUEPRINT, version='1.0', title='FLASK Backend API', description='FLASK Backend API')
