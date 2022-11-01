from fastapi import HTTPException, Depends
from typing import List
from uuid import UUID
from sqlalchemy.orm import Session
from domain.Stock import Stock, StockDto, StockModel
from infrastructure.database import get_db_connection

class StockRepository:

    db : Session

    def __init__(self, db: Session = Depends(get_db_connection)):
        self.db = db

    async def get(self) -> List[Stock]:
        return self.db.query(StockModel).all()

    async def find(self, id: UUID) -> Stock:
        product = self.db.query(StockModel).filter(StockModel.id == str(id)).first()
        if product is None:
            raise HTTPException(status_code=404, detail="Stock not found")
        return product
    
    async def find_by_product(self, product_id: UUID) -> Stock:
        product = self.db.query(StockModel).filter(StockModel.product_id == str(product_id)).first()
        if product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        return product
       

    async def create(self, stock: Stock) -> Stock:
        stock_model = StockModel(id = str(stock.id), product_id = stock.product_id ,quantity = stock.quantity )
        self.db.add(stock_model)
        self.commit()
        return stock_model

    async def delete(self, id: UUID) -> None:
        stock = await self.find(id)
        self.db.delete(stock)
        self.commit()

    async def update(self, id: UUID, quantity: int) -> Stock:
        prev_stock = await self.find(id)
        prev_stock.quantity = quantity
        self.commit()
        return prev_stock

    def commit(self):
        return self.db.commit()