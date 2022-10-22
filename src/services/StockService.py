from typing import List
from unicodedata import name
import uuid
from fastapi import Depends, HTTPException

from domain.Stock import Stock
from dto.StockDto import StockDto
from repositories.StockRepository import StockRepository
from routers.ProductRouter import delete
from services.ProductService import ProductService


class StockService:

    def __init__(
        self,
        stockRepository: StockRepository = Depends(),
        productService: ProductService = Depends()
    ) -> None:
        self.stockRepository = stockRepository
        self.productService = productService

    async def get(self) -> List[Stock]:
        return await self.stockRepository.get()

    async def find(self, id: uuid.UUID) -> Stock:
        return await self.stockRepository.find(id)

    async def create_or_add(self, stock: StockDto) -> Stock:
        if await self.productService.find(stock.product_id) is None:
            raise HTTPException(status_code=404, detail="Product not registered")

        st = await self.stockRepository.find_by_product(stock.product_id)
        if st is None:
            new_stock = self._generate_stock(stock)
            return await self.stockRepository.create(new_stock)
    
        st.quantity += 1
        return await self.stockRepository.update(st.id, st)
    
    async def delete_or_sub(self, id: uuid.UUID) -> None:
        st = await self.stockRepository.find(id)
        st.quantity -= 1
        if st.quantity == 0:
            return await self.stockRepository.delete(id)
        
        return await self.stockRepository.update(id, st)

    def _generate_stock(self, stock: StockDto):
        generated_id = uuid.uuid5(uuid.NAMESPACE_DNS, str(stock.product_id))
        return Stock(
            id = generated_id,
            product_id = stock.product_id
        )
