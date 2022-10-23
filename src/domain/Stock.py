from itertools import product
from turtle import title
from pydantic import Field
import uuid as uuid_pkg
from domain.base.UUIDBaseModel import UUIDBaseModel

class Stock(UUIDBaseModel):

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

    def add():
        quantity += 1
    


