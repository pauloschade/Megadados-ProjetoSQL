from typing import List
import uuid
from fastapi import Depends, HTTPException
from domain.Stock import Stock, StockDto
from repositories.StockRepository import StockRepository
from repositories.ProductRepository import ProductRepository


class StockService:

    def __init__(
        self,
        stockRepository: StockRepository = Depends(),
        productRepository: ProductRepository = Depends()
    ) -> None:
        self.stockRepository = stockRepository
        self.productRepository = productRepository

    async def get(self) -> List[Stock]:
        return await self.stockRepository.get()

    async def find(self, id: uuid.UUID) -> Stock:
        return await self.stockRepository.find(id)
    
    async def update(self, id: uuid.UUID, quantity: int) -> Stock:
        updated_st = await self.stockRepository.update(id, quantity)
        self.stockRepository.commit()
        return updated_st

    async def create(self, stock: StockDto) -> Stock:
        product = await self.productRepository.find(stock.product_id)
        new_stock = self._generate_stock(stock)
        try:
            stock = await self.stockRepository.find_by_product(product.id)
        except:
            created_st = await self.stockRepository.create(new_stock)
            self.stockRepository.commit()
            return created_st
        raise HTTPException(status_code=400, detail=f"Product with id {product.id} already in stock")


        
    
    async def delete(self, id: uuid.UUID) -> None:
        await self.stockRepository.delete(id)
        self.stockRepository.commit()

    def _generate_stock(self, stock: StockDto):
        return Stock(
            product_id = stock.product_id,
            quantity = stock.quantity
        )
