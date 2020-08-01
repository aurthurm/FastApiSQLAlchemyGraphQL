from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr
from .session import GQLSessionLocal


@as_declarative()
class Base:
    id: Any
    __name__: str
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

# We will need this for querying
Base.query = GQLSessionLocal.query_property()