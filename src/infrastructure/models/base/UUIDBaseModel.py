
from sqlalchemy.schema import Column
from sqlalchemy import String
from sqlalchemy.dialects.mysql import UUID



class UUIDBaseModel():
    id  = Column(UUID, primary_key=True)