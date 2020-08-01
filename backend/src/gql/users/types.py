from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene import relay
from apps.user.models import User

# Graphene User Type
class UserType(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node, )