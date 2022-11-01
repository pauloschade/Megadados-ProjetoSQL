from typing import List
from unicodedata import name
import uuid
from fastapi import Depends

from domain.Product import Product
from domain.Product import ProductDto
from repositories.ProductRepository import ProductRepository


class ProductService:

    def __init__(
        self, productRepository: ProductRepository = Depends()
    ) -> None:
        self.productRepository = productRepository

    async def get(self) -> List[Product]:
        return await self.productRepository.get()

    async def find(self, id: uuid.UUID) -> Product:
        return await self.productRepository.find(id)

    async def create(self, product: ProductDto) -> Product:
        new_product = self._generate_product(product)
        return await self.productRepository.create(new_product)

    async def delete(self, id: uuid.UUID) -> None:
        return await self.productRepository.delete(id)

    async def update(self, id: uuid.UUID, product: ProductDto) -> Product:
        return await self.productRepository.update(id, product)

    def _generate_product(self, product: ProductDto):
        return Product(
            name=product.name, 
            price = product.price, 
            description = product.description
        )
