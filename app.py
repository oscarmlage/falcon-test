import falcon
from sqlalchemy import create_engine
from falcon_autocrud.middleware import Middleware

import log
import config
import models

from api.v1 import (athletes, categories, countries, disciplines, locations,
                    referees, rounds, sessions, teams)


LOG = log.get_logger()


db_engine = create_engine(config.DATABASE_URL)
LOG.info('Connecting to database.')

models.Base.metadata.drop_all(db_engine)
LOG.info('Dropping existing database schema.')

models.Base.metadata.create_all(db_engine)
LOG.info('Creating database schema.')

api = falcon.API(middleware=Middleware())
LOG.info('API Server started.')

# DB resources
api.add_route('/athletes', athletes.AthleteCollectionResource(db_engine))
api.add_route('/athletes/{id}', athletes.AthleteResource(db_engine))

api.add_route('/categories', categories.CategoryCollectionResource(db_engine))
api.add_route('/categories/{id}', categories.CategoryResource(db_engine))

api.add_route('/countries', countries.CountryCollectionResource(db_engine))
api.add_route('/countries/{id}', countries.CountryResource(db_engine))

api.add_route('/disciplines',
              disciplines.DisciplineCollectionResource(db_engine))
api.add_route('/disciplines/{id}', disciplines.DisciplineResource(db_engine))

api.add_route('/locations', locations.LocationCollectionResource(db_engine))
api.add_route('/locations/{id}', locations.LocationResource(db_engine))

api.add_route('/referees', referees.RefereeCollectionResource(db_engine))
api.add_route('/referees/{id}', referees.RefereeResource(db_engine))

api.add_route('/rounds', rounds.RoundCollectionResource(db_engine))
api.add_route('/rounds/{id}', rounds.RoundResource(db_engine))

api.add_route('/sessions', sessions.SessionCollectionResource(db_engine))
api.add_route('/sessions/{id}', sessions.SessionResource(db_engine))

api.add_route('/teams', teams.TeamCollectionResource(db_engine))
api.add_route('/teams/{id}', teams.TeamResource(db_engine))
