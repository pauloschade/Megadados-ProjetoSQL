from fastapi import HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from uuid import UUID
from domain.Product import Product, ProductDto, ProductModel
from infrastructure.database import get_db_connection

class ProductRepository:

    db : Session

    def __init__(self, db: Session = Depends(get_db_connection)):
        self.db = db

    async def get(self) -> List[Product]:
       return self.db.query(ProductModel).all()

    async def find(self, id: UUID) -> Product:
        product = self.db.query(ProductModel).filter(ProductModel.id == str(id)).first()
        if product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        return product
       

    async def create(self, product: Product) -> Product:
        product_model = ProductModel(id = str(product.id), name = product.name, price = product.price, description=product.description)
        self.db.add(product_model)
        return product_model

    async def delete(self, id: UUID) -> None:
        product = await self.find(id)
        self.db.delete(product)

    async def update(self, id: UUID, product: ProductDto) -> Product:
        prev_product = await self.find(id)
        prev_product.name = product.name
        prev_product.price = product.price
        prev_product.description = product.description
        return prev_product

    def commit(self):
        return self.db.commit()