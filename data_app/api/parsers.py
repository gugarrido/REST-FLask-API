from flask_restx import reqparse

get_foo_args = reqparse.RequestParser()
get_foo_args.add_argument(
    'foo',
    type=str,
    required=True,
    help='foo value'
)
