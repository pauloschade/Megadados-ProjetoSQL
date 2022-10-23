from fastapi import HTTPException
from typing import List
from uuid import UUID
from dto.ProductDto import ProductDto
from domain.Product import Product
from db.product_db import fake_product_db
class ProductRepository:

    async def get(self) -> List[Product]:
        return fake_product_db

    async def find(self, id: UUID) -> Product:
        for i in fake_product_db:
            if i.id == id:
                return i
        return None
       

    async def create(self, product: Product) -> Product:
        fake_product_db.append(product)

    async def delete(self, id: UUID) -> None:
        for i in range(len(fake_product_db)):
            if fake_product_db[i].id == id:
                fake_product_db.pop(i)
                return
        raise HTTPException(status_code=404, detail="Product not found")

    async def update(self, id: UUID, product: ProductDto) -> Product:
        for i in range(len(fake_product_db)):
            if fake_product_db[i].id == id:
                fake_product_db[i].name = product.name
                fake_product_db[i].price = product.price
                fake_product_db[i].description = product.description
                return product
        raise HTTPException(status_code=404, detail="Product not found")