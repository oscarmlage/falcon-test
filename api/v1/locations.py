from falcon_autocrud.resource import CollectionResource, SingleResource
from models import Location


class LocationCollectionResource(CollectionResource):
    model = Location
    methods = ['GET', 'POST']


class LocationResource(SingleResource):
    model = Location
    default_sort = ['name']
