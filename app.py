import falcon
from sqlalchemy import create_engine
from falcon_autocrud.resource import CollectionResource, SingleResource
from falcon_autocrud.middleware import Middleware


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


db_engine = create_engine('sqlite:///stuff.db')
api = falcon.API(middleware=Middleware())

api.add_route('/one', ObjReq())
api.add_route('/two', ObjReqNew())
api.add_route('/quote', QuoteResource())

api.add_route('/notes', NoteCollectionResource(db_engine))
api.add_route('/notes/{id}', NoteResource(db_engine))
