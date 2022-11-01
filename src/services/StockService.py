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
        return await self.stockRepository.update(id, quantity)

    async def create(self, stock: StockDto) -> Stock:
        product = await self.productRepository.find(stock.product_id)
        new_stock = self._generate_stock(stock)
        try:
            stock = await self.stockRepository.find_by_product(product.id)
            raise HTTPException(status_code=404, detail=f"Product with id {product.id} already in stock")
        except:
            return await self.stockRepository.create(new_stock)


        
    
    async def delete(self, id: uuid.UUID) -> None:
        return await self.stockRepository.delete(id)

    def _generate_stock(self, stock: StockDto):
        return Stock(
            product_id = stock.product_id,
            quantity = stock.quantity
        )
