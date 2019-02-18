from falcon_autocrud.resource import CollectionResource, SingleResource
from models import Country


class CountryCollectionResource(CollectionResource):
    model = Country
    methods = ['GET', 'POST']


class CountryResource(SingleResource):
    model = Country
    default_sort = ['name']
