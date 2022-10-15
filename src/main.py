from typing import Union

from fastapi import Depends, FastAPI

from routers.ProductRouter import ProductRouter

app = FastAPI()

# Add Routers
app.include_router(ProductRouter)
