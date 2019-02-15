import falcon
from sqlalchemy import create_engine
from falcon_autocrud.middleware import Middleware

import log
import config

from api.v1 import statics
from api.v1 import notes


LOG = log.get_logger()


db_engine = create_engine(config.DATABASE_URL)
LOG.info('Connecting to database.')

api = falcon.API(middleware=Middleware())
LOG.info('API Server started.')

# Static resources
api.add_route('/help', statics.HelpResource())
api.add_route('/quote', statics.QuoteResource())

# DB resources
api.add_route('/notes', notes.NoteCollectionResource(db_engine))
api.add_route('/notes/{id}', notes.NoteResource(db_engine))
