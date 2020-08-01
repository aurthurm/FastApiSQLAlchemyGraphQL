import graphene
from fastapi import Depends
from graphene import String
from graphql import GraphQLError
from sqlalchemy.orm import Session

from apps.item.crud import aitem, item
from gql.items.types import ItemType

from database.session import GQLSessionLocal
from database.session import database as async_db

sync_db = GQLSessionLocal.session_factory()

class CreateItem(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        # token = graphene.String(required=True)

    ok = graphene.Boolean()
    stuff = graphene.Field(lambda: ItemType)

    def mutate(root, info, title, description, db: Session = sync_db):
        payload = {"title": title, "description": description}
        _item = item.create(db, obj_in=payload)
        ok = True
        return CreateItem(ok=ok, stuff=_item)


class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        fullname = graphene.String()

    ok = graphene.Boolean()
    user = graphene.Field(lambda: UserInfoSchema)

    @staticmethod
    def mutate(root, info, username, password, fullname, ):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user = UserInfoSchema(username=username, password=hashed_password, fullname=fullname)
        ok = True
        db_user = crud.get_user_by_username(db, username=username)
        if db_user:
            raise GraphQLError("Username already registered")
        user_info = UserCreate(username=username, password=password, fullname=fullname)
        crud.create_user(db, user_info)
        return CreateUser(user=user, ok=ok)


class AuthenUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    token = graphene.String()

    @staticmethod
    def mutate(root, info, username, password):
        db_user = crud.get_user_by_username(db, username=username)
        user_authenticate = UserAuthenticate(username=username, password=password)
        if db_user is None:
            raise GraphQLError("Username not existed")
        else:
            is_password_correct = crud.check_username_password(db, user_authenticate)
            if is_password_correct is False:
                raise GraphQLError("Password is not correct")
            else:
                from datetime import timedelta
                access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
                from app_utils import create_access_token
                access_token = create_access_token(
                    data={"sub": username}, expires_delta=access_token_expires)
                return AuthenUser(token=access_token)