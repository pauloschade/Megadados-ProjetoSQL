from fastapi import FastAPI

from routers.ProductRouter import ProductRouter
from routers.StockRouter import StockRouter

app = FastAPI()

# Add Routers
app.include_router(ProductRouter)
app.include_router(StockRouter)
