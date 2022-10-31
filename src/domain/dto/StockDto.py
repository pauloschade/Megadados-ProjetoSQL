from itertools import product
from typing import Optional
from pydantic import BaseModel
import uuid as uuid_pkg
class StockDto(BaseModel):
    """
    Class for requests regarding stock
    """
    product_id :  uuid_pkg.UUID
    quantity : Optional[int]