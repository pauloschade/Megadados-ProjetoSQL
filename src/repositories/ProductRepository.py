from pydoc import describe
from typing import List, Optional
from uuid import UUID
from fastapi import Depends

from domain.Product import Product

fake_db = []
class ProductRepository:
    #TODO

    async def get(self) -> List[Product]:
        return fake_db

    async def find(self, id: UUID) -> Product:
       #TODO
       new_product = Product(name = "teste find", price = 2)
       return new_product
       

    async def create(self, product: Product) -> Product:
        fake_db.append(product)

    async def delete(self, id: UUID) -> None:
        #TODO
        pass

    async def update(self, id: UUID, product: Product) -> Product:
        #TODO
        pass