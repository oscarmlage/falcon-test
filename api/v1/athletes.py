from falcon_autocrud.resource import CollectionResource, SingleResource
import models


class AthleteCollectionResource(CollectionResource):
    model = models.Athlete
    methods = ['GET', 'POST']


class AthleteResource(SingleResource):
    model = models.Athlete
    default_sort = ['name']
