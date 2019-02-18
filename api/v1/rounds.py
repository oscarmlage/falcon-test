from falcon_autocrud.resource import CollectionResource, SingleResource
from models import Round


class RoundCollectionResource(CollectionResource):
    model = Round
    methods = ['GET', 'POST']


class RoundResource(SingleResource):
    model = Round
    default_sort = ['name']
