from pydantic import Field
from uuid import UUID
from typing import Optional
from domain.base.UUIDBaseModel import UUIDBaseModel

class Product(UUIDBaseModel):

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

