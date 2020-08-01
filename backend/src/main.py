from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from graphql.execution.executors.asyncio import AsyncioExecutor

from database.session import database

from api.api_v1.api import api_router
from core.config import settings

from starlette.graphql import GraphQLApp
from gql.schema import gql_schema


app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    
# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)
app.add_route("/graphql", GraphQLApp(schema=gql_schema, executor_class=AsyncioExecutor))
