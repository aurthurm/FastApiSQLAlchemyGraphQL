# Import all the models, so that Base has them before being
# imported by Alembic
try:
    from database.base_class import Base  # noqa
    from apps.item.models import Item  # noqa
    from apps.user.models import User  # noqa
except ModuleNotFoundError:
    from src.database.base_class import Base  # noqa
    from src.apps.item.models import Item  # noqa
    from src.apps.user.models import User  # noqa
