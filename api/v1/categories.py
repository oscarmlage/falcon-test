from falcon_autocrud.resource import CollectionResource, SingleResource
from models import Category


class CategoryCollectionResource(CollectionResource):
    model = Category
    methods = ['GET', 'POST']


class CategoryResource(SingleResource):
    model = Category
    default_sort = ['name']
