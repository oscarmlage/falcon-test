from falcon_autocrud.resource import CollectionResource, SingleResource
import models


class NoteCollectionResource(CollectionResource):
    model = models.Note
    methods = ['GET', 'POST']


class NoteResource(SingleResource):
    model = models.Note
    default_sort = ['title']
