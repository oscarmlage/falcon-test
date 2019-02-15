import falcon, json


class ObjReq:
    def on_get(self, req, resp):
        content = {
            'name': 'Oscar',
            'age': 'Unknown'
        }
        resp.body = json.dumps(content)


class ObjReqNew:
    def on_get(self, req, resp):
        content = {
            'name': 'John Doe',
            'age': 33
        }
        resp.body = json.dumps(content)


api = falcon.API()
api.add_route('/two', ObjReq())
api.add_route('/one', ObjReqNew())
