from falcon_autocrud.resource import CollectionResource, SingleResource
from models import Team


class TeamCollectionResource(CollectionResource):
    model = Team
    methods = ['GET', 'POST']


class TeamResource(SingleResource):
    model = Team
    default_sort = ['name']
