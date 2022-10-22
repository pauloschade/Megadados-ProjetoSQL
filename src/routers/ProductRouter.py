from typing import List, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, status

from domain.Product import Product
from dto.ProductDto import ProductDto
from services.ProductService import ProductService

ProductRouter = APIRouter(
    prefix="/products", tags=["product"]
)


@ProductRouter.get(
    "/", 
    response_model=List[Product],
    summary = "Gets all registered products",
    description = "Returns all products that are registered.\n \
    IMPORTANT: even if we are out of any products, meaning that they are SOLD OUT, they will be returned by this endpoint"
)
async def index(productService: ProductService = Depends()):
    return await productService.get()


@ProductRouter.get(
    "/{id}", 
    response_model=Product,
    summary = "Gets a registered product",
    description = "Returns the product with the specified ID.\n \
        IMPORTANT: even if the product is SOLD OUT, it will be returned"
)
async def get(id: UUID, productService: ProductService = Depends()):
    return await productService.find(id)


@ProductRouter.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    summary = "Registers a product"
)
async def create(
    product: ProductDto,
    productService: ProductService = Depends(),
):
    return await productService.create(product)


@ProductRouter.put(
    "/{id}", 
    response_model=Product,
    summary = "Updates the details of a product",
    description = "Takes in an ID and changes the product details"
)
async def update(
    id: UUID,
    product: ProductDto,
    productService: ProductService = Depends(),
):
    return await productService.update(id, product)


@ProductRouter.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary = "Deletes a product",
    description = "Deletes the product with the given ID.\n \
        IMPORTANT: If the product is available in stock, it will be erased there"
)
async def delete(
    id: UUID, productService: ProductService = Depends()
):
    return await productService.delete(id)