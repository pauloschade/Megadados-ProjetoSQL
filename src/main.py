from fastapi import FastAPI

from routers.ProductRouter import ProductRouter

app = FastAPI()

# Add Routers
app.include_router(ProductRouter)
