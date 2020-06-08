from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

RESULTS = {
    'todo__no1': '11111',
    'todo__no2': '22222',
    'todo__no3': '33333',
}


def abort_if_path_not_exist(path):
    if path not in RESULTS:
        abort(404, message="{} doesn't exist".format(path.replace("__", "/")))


def redirect_if_path_is_special(path):
    if path == '/api/records':
        return True
    else:
        return False


parser = reqparse.RequestParser()
parser.add_argument('path')
parser.add_argument('resp')


class Api(Resource):
    def get(self, path):
        abort_if_path_not_exist(path)
        return RESULTS[path]

    def post(self, path):
        abort_if_path_not_exist(path)
        return RESULTS[path]

    def delete(self, path):
        abort_if_path_not_exist(path)
        del RESULTS[path]
        return {'status': "deleted"}, 204

    def put(self, path):
        args = parser.parse_args()
        RESULTS[path] = args['resp']
        return {'status': "added"}, 201


class ApiList(Resource):
    def get(self):
        return RESULTS

    def post(self):
        args = parser.parse_args()
        path = args['path']
        RESULTS[path] = args['resp']
        return RESULTS[path], 201


api.add_resource(ApiList, '/api/records')
api.add_resource(Api, '/<path>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
