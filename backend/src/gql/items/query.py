import graphene
from graphene import (
    relay,
    String,
)
from graphql import GraphQLError
from graphene_sqlalchemy import SQLAlchemyConnectionField

from .types import ItemType
from apps.item.models import Item

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    #
    all_items = SQLAlchemyConnectionField(ItemType.connection)
    wonke_items = graphene.List(ItemType)

    async def resolve_wonke_items(self, info):
        wonke = ItemType.get_query(info)
        return wonke.all()