import uuid as uuid_pkg
from pydantic import Field, BaseModel

from sqlalchemy.schema import Column
from sqlalchemy import String

class UUIDBase(BaseModel):
    
    id: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )


class UUIDBaseModel():
    id  = Column(String(50), primary_key=True)