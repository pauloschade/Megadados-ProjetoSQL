from fastapi import HTTPException
from typing import List
from uuid import UUID
from domain.Stock import Stock
from db.stock_db import fake_stock_db

class StockRepository:
    #TODO

    async def get(self) -> List[Stock]:
        return fake_stock_db

    async def find(self, id: UUID) -> Stock:
        for i in fake_stock_db:
            if i.id == id:
                return i
        return None
    
    async def find_by_product(self, product_id: UUID) -> Stock:
        for i in fake_stock_db:
            if i.product_id == product_id:
                return i
        return None
       

    async def create(self, stock: Stock) -> Stock:
        fake_stock_db.append(stock)

    async def delete(self, id: UUID) -> None:
        for i in range(len(fake_stock_db)):
            if fake_stock_db[i].id == id:
                fake_stock_db.pop(i)
                return
        raise HTTPException(status_code=404, detail="Stock not found")

    async def update(self, id: UUID, quantity: int) -> Stock:
        for i in range(len(fake_stock_db)):
            print(id)
            if fake_stock_db[i].id == id:
                fake_stock_db[i].quantity = quantity
                return fake_stock_db[i]
        raise HTTPException(status_code=404, detail="Stock not found")