from pydoc import describe
from typing import List, Optional
from uuid import UUID
from fastapi import Depends

from domain.Product import Product


class ProductRepository:
    #TODO

    async def get(self) -> List[Product]:
        #TODO
        new_product = Product(name = "teste get", price = 1)
        return [new_product]

    async def find(self, id: UUID) -> Product:
       #TODO
       new_product = Product(name = "teste find", price = 2)
       return new_product
       

    async def create(self, product: Product) -> Product:
        #TODO
        pass

    async def delete(self, id: UUID) -> None:
        #TODO
        pass

    async def update(self, id: UUID, product: Product) -> Product:
        #TODO
        pass