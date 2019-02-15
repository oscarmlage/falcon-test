import falcon


class ObjReq:
    def on_get(self, req, resp):
        content = {
            'name': 'Oscar',
            'age': 'Unknown'
        }
        resp.media = content


class ObjReqNew:
    def on_get(self, req, resp):
        content = {
            'name': 'John Doe',
            'age': 33
        }
        resp.media = content


class QuoteResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            'quote': (
                "I've always been more interested in "
                "the future than in the past."
            ),
            'author': 'Grace Hopper'
        }

        resp.media = quote


api = falcon.API()
api.add_route('/two', ObjReq())
api.add_route('/one', ObjReqNew())
api.add_route('/quote', QuoteResource())
