import graphene
from graphene import String
from graphql import GraphQLError

from app.apps.item import schemas, models # noqa
from app.gql.items import query as item_query # noqa
from app.gql.items import mutations as item_mutations # noqa

from app.apps.user import schemas, models # noqa
from app.gql.users import query as user_query # noqa
from app.gql.users import mutations as user_mutations # noqa

class Query(
    user_query.Query, 
    item_query.Query, 
    graphene.ObjectType
):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class Mutation(graphene.ObjectType):
    itemcreate = item_mutations.CreateItem.Field()
    #Users
    usercreate = user_mutations.CreateUser.Field()
    userauthenticate = user_mutations.AuthenticateUser.Field()
    userupdate = user_mutations.UpdateUser.Field()
    recoverpassword = user_mutations.RecoverPassword.Field()
    

gql_schema = graphene.Schema(query=Query, mutation=Mutation)