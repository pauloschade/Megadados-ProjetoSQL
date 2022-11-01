from pydantic import Field, BaseModel
from typing import Optional
from domain.base.UUIDBase import UUIDBase, UUIDBaseModel
from sqlalchemy.schema import Column
from sqlalchemy import String, Float
from infrastructure.database import Base

class Product(UUIDBase):

    """
    Class for products to be registered
    """

    name : str = Field(
        title = 'Product name',
        max_length=1024,
    )

    price : float = Field(
        title = 'Product price',
    )

    description : Optional[str] = Field(
        title='Product description',
        max_length=1024,
    )

    class Config:
        orm_mode = True

class ProductDto(BaseModel):

    """
    Class for requests regarding products
    """

    name : str = Field(
        title = 'Product name',
        max_length=1024,
    )

    price : float = Field(
        title = 'Product price',
    )

    description : Optional[str] = Field(
        title='Product description',
        max_length=1024,
    )


class ProductModel(Base, UUIDBaseModel):

    __tablename__ = "Product"

    name = Column(String(30))

    price = Column(Float)

    description = Column(String(30), nullable = True)
