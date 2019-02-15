import falcon
from sqlalchemy import create_engine
from falcon_autocrud.middleware import Middleware


from api.v1 import statics
from api.v1 import notes


db_engine = create_engine('sqlite:///stuff.db')
api = falcon.API(middleware=Middleware())

# Static resources
api.add_route('/help', statics.HelpResource())
api.add_route('/quote', statics.QuoteResource())

# DB resources
api.add_route('/notes', notes.NoteCollectionResource(db_engine))
api.add_route('/notes/{id}', notes.NoteResource(db_engine))
