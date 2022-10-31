from models.base.UUIDBaseModel import UUIDBaseModel
from sqlalchemy.schema import Column
from sqlalchemy import String, Float
from infrastructure.database import Base

class ProductModel(UUIDBaseModel, Base):

    __tablename__ = "Product"

    name = Column(String(30))

    price = Column(Float)

    description = Column(String(30), nullable = True)