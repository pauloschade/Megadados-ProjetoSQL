from typing import List, Optional
from uuid import UUID
from fastapi import Depends

from domain.Product import Product
from repositories.ProductRepository import ProductRepository


class ProductService:

    def __init__(
        self, productRepository: ProductRepository = Depends()
    ) -> None:
        self.productRepository = productRepository

    async def get(self) -> List[Product]:
        return await self.productRepository.get()

    async def find(self, id: UUID) -> Product:
        return await self.productRepository.find(id)

    async def create(self, product: Product) -> Product:
        return await self.productRepository.create(Product)

    async def delete(self, id: UUID) -> None:
        return await self.productRepository.delete(id)

    async def update(self, id: UUID, product: Product) -> Product:
        return await self.productRepository.update(id, product)