import uuid as uuid_pkg
from pydantic import BaseModel, Field

class UUIDBaseModel(BaseModel):
    
    id: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )