from itertools import product
from pydantic import Field, BaseModel
from typing import Optional
import uuid as uuid_pkg
from domain.base.UUIDBase import UUIDBase, UUIDBaseModel
from infrastructure.database import Base
from sqlalchemy.schema import Column
from sqlalchemy.orm import relationship, backref
from sqlalchemy import String, Integer, ForeignKey, CheckConstraint

class Stock(UUIDBase):

    """
    Class for products in stock
    """

    product_id : uuid_pkg.UUID = Field(
        title = 'Product in stock'
    )

    quantity : int = Field(
        default = 1,
        title = 'Quantity of product in stock'
    )
    class Config:
        orm_mode = True

class StockDto(BaseModel):
    """
    Class for requests regarding stock
    """
    product_id :  uuid_pkg.UUID
    quantity : Optional[int]


class StockModel(UUIDBaseModel, Base):

    __tablename__ = "Stock"
    product_id = Column(String(50), ForeignKey("Product.id", ondelete='CASCADE'), nullable=False)
    quantity = Column(Integer)
    __table_args__ = (
        CheckConstraint(quantity >= 0, name='check_quantity_positive'),
    {})

    Product = relationship("ProductModel", backref=backref("StockModel", cascade="all,delete"))


