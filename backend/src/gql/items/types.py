from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene import relay
from apps.item.models import Item

# Graphene Item Type
class ItemType(SQLAlchemyObjectType):
    class Meta:
        model = Item
        interfaces = (relay.Node, )