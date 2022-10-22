from itertools import product
from pydantic import BaseModel
import uuid as uuid_pkg
from typing import Optional

class StockDto(BaseModel):
    product_id :  uuid_pkg.UUID