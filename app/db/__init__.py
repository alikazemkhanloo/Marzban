from sqlalchemy.orm import Session
from .base import Base, SessionLocal, engine  # noqa

from fastapi import Depends


class GetDB:  # Context Manager
    def __init__(self):
        self.db = SessionLocal()

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()


def get_db():  # Dependency
    with GetDB() as db:
        yield db


from .models import ClientStatus
from .models import Admin
from .models import Client
from .models import ClientDataLimitResetStrategy
from .models import ClientUsageResetLogs
from .models import Inbound
from .models import InboundClientSettings
from .models import ClientStatus
from .models import InboundSettings
