from typing import List
from unicodedata import name
import uuid
from fastapi import Depends, HTTPException

from domain.Stock import Stock
from dto.StockDto import StockDto
from repositories.StockRepository import StockRepository
from routers.ProductRouter import delete
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
    
    async def update(self, id: uuid.UUID, stock: StockDto) -> Stock:
        new_stock = self._generate_stock(stock)
        return await self.stockRepository.update(id, new_stock)

    async def create_or_add(self, stock: StockDto) -> Stock:
        if await self.productRepository.find(stock.product_id) is None:
            raise HTTPException(status_code=404, detail="Product not registered")

        st = await self.stockRepository.find_by_product(stock.product_id)
        if st is None:
            new_stock = self._generate_stock(stock)
            return await self.stockRepository.create(new_stock)
        
        if stock.quantity is None:
            st.quantity += 1
        else:
            st.quantity += stock.quantity
        return await self.stockRepository.update(st.id, st)
    
    async def delete(self, id: uuid.UUID) -> None:
        return await self.stockRepository.delete(id)

    def _generate_stock(self, stock: StockDto):
        generated_id = uuid.uuid5(uuid.NAMESPACE_DNS, str(stock.product_id))
        return Stock(
            id = generated_id,
            product_id = stock.product_id,
            quantity = stock.quantity
        )
