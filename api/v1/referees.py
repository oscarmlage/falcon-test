from falcon_autocrud.resource import CollectionResource, SingleResource
from models import Referee


class RefereeCollectionResource(CollectionResource):
    model = Referee
    methods = ['GET', 'POST']


class RefereeResource(SingleResource):
    model = Referee
    default_sort = ['name']
