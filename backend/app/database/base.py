# Import all the models, so that Base has them before being
# imported by Alembic

from app.database.base_class import Base  # noqa
from app.apps.item.models import Item  # noqa
from app.apps.user.models import User  # noqa
