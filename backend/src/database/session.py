import databases
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
try:
    from src.core.config import settings
except ModuleNotFoundError:
    from core.config import settings


database = databases.Database(settings.SQLALCHEMY_DATABASE_URI)

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
GQLSessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
