from typing import List, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, status

from domain.Product import Product
from dto.ProductDto import ProductDto
from services.ProductService import ProductService

ProductRouter = APIRouter(
    prefix="/products", tags=["product"]
)


@ProductRouter.get("/", response_model=List[Product])
async def index(productService: ProductService = Depends()):
    return await productService.get()


@ProductRouter.get("/{id}", response_model=Product)
async def get(id: UUID, productService: ProductService = Depends()):
    return await productService.find(id)


@ProductRouter.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
async def create(
    product: ProductDto,
    productService: ProductService = Depends(),
):
    return await productService.create(product)


@ProductRouter.patch("/{id}", response_model=Product)
async def update(
    id: UUID,
    product: ProductDto,
    productService: ProductService = Depends(),
):
    return await productService.update(id, product)


@ProductRouter.delete(
    "/{id}", status_code=status.HTTP_204_NO_CONTENT
)
async def delete(
    id: UUID, productService: ProductService = Depends()
):
    return await productService.delete(id)