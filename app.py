import falcon
from falcon_autocrud.resource import CollectionResource, SingleResource

from middleware import DatabaseSessionManager
from database import db_session, init_session, engine

from models import Note


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


class NoteCollectionResource(CollectionResource):
    model = Note
    methods = ['GET', 'POST']


class NoteResource(SingleResource):
    model = Note
    default_sort = ['title']


init_session()

middleware = [DatabaseSessionManager(db_session)]

api = falcon.API(middleware=middleware)

api.add_route('/two', ObjReq())
api.add_route('/one', ObjReqNew())
api.add_route('/quote', QuoteResource())

api.add_route('/notes', NoteCollectionResource(engine))
api.add_route('/notes/{id}', NoteResource(engine))
