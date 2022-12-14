from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, status

from domain.Stock import Stock, StockDto
from services.StockService import StockService

StockRouter = APIRouter(
    prefix="/stocks", tags=["stock"]
)


@StockRouter.get(
    "/", 
    response_model=List[Stock],
    summary = "Gets all stock",
    description = "If the product is available on stock, it will be returned by this endpoint"
)
async def index(stockService: StockService = Depends()):
    return await stockService.get()


@StockRouter.get(
    "/{id}", 
    response_model=Stock,
    summary = "Gets the id of a product and quantity (if available) in stock"
)
async def get(id: UUID, stockService: StockService = Depends()):
    return await stockService.find(id)


@StockRouter.post(
    "/",
    response_model = Stock,
    status_code=status.HTTP_201_CREATED,
    summary = "Adds a product to stock"
)
async def create(
    stock: StockDto,
    StockService: StockService = Depends(),
):
    return await StockService.create(stock)

@StockRouter.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary = "Removes a product from stock"
)
async def delete(
    id: UUID, StockService: StockService = Depends()
):
    return await StockService.delete(id)

@StockRouter.patch(
    "/{id}",
    summary = "Updates a stock quantity"
)
async def update(
    id: UUID,
    quantity: int,
    StockService: StockService = Depends()
):
    return await StockService.update(id, quantity)
