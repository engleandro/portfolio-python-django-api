import graphene
from graphene_django import DjangoObjectType

from main.models import BaseModel

class GrapheneBaseModel(DjangoObjectType):
    class Meta:
        model = BaseModel

class Query(graphene.ObjectType):
    users = graphene.List(GrapheneBaseModel)

    def resolve_users(self, info):
        return BaseModel.objects.all()

schema = graphene.Schema(query=Query)