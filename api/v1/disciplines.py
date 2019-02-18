from falcon_autocrud.resource import CollectionResource, SingleResource
from models import Discipline


class DisciplineCollectionResource(CollectionResource):
    model = Discipline
    methods = ['GET', 'POST']


class DisciplineResource(SingleResource):
    model = Discipline
    default_sort = ['name']
