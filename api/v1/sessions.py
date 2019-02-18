from falcon_autocrud.resource import CollectionResource, SingleResource
from models import Session


class SessionCollectionResource(CollectionResource):
    model = Session
    methods = ['GET', 'POST']


class SessionResource(SingleResource):
    model = Session
    default_sort = ['name']
