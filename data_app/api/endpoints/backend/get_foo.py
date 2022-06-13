from data_app.api.restplus import API
from flask_restx import Resource
from data_app.api.parsers import get_foo_args


ns = API.namespace('get_foo', description='return foo')


@ns.route('/')
class GetFoo(Resource):
    @API.expect(get_foo_args)
    def get(self):
        ns.logger.debug("hit get_foo endpoint")
        args = get_foo_args.parse_args()
        if args:
            return args, 200