from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

recordMap = {}


def get_record_list():
    return [x.json() for x in recordMap.values()]


class ApiRecord:
    def __init__(self, path, resp_data, show_type):
        self.path = path
        self.resp_data = resp_data
        self.show_type = show_type

    def json(self):
        return {"path": self.path, "resp_data": self.resp_data, "show_type": self.show_type}

    def resp_show(self):
        if self.show_type == "1":
            return self.resp_data


def abort_if_path_not_exist(path):
    if path not in recordMap:
        abort(404, message="{} doesn't exist".format(path.replace("__", "/")))


def redirect_if_path_is_special(path):
    if path == '/api/records':
        return True
    else:
        return False


parser = reqparse.RequestParser()
parser.add_argument('path')
parser.add_argument('resp_data')
parser.add_argument('show_type')


class Api(Resource):
    def get(self, path):
        abort_if_path_not_exist(path)
        return recordMap[path].resp_show()

    def post(self, path):
        abort_if_path_not_exist(path)
        return recordMap[path].resp_show()

    def delete(self, path):
        abort_if_path_not_exist(path)
        del recordMap[path]
        return {'status': "deleted"}, 204

    def put(self, path):
        args = parser.parse_args()
        resp_data = args['resp_data']
        show_type = args['show_type']
        recordMap[path] = ApiRecord(path, resp_data, show_type)
        return {'status': "added"}, 201


class ApiList(Resource):
    def get(self):
        return get_record_list

    def post(self):
        args = parser.parse_args()
        path = args['path']
        resp_data = args['resp_data']
        show_type = args['show_type']
        recordMap[path] = ApiRecord(path, resp_data, show_type)
        return recordMap[path].resp_show(), 201


api.add_resource(ApiList, '/api/records')
api.add_resource(Api, '/<path>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
