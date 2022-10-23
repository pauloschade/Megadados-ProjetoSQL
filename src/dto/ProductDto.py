from pydantic import BaseModel, Field
from typing import Optional

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