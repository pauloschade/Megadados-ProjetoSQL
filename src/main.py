from fastapi import FastAPI

from infrastructure.routers.ProductRouter import ProductRouter
from infrastructure.routers.StockRouter import StockRouter

app = FastAPI()

# Add Routers
app.include_router(ProductRouter)
app.include_router(StockRouter)
