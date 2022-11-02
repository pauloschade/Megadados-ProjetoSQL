from typing import List, Optional
from uuid import UUID
from fastapi import APIRouter, Depends, status
from domain.Transaction import Transaction, TransactionDto
from services.TransactionService import TransactionService

TransactionRouter = APIRouter(
    prefix="/transactions", tags=["tx"]
)


@TransactionRouter.get(
    "/", 
    response_model=List[Transaction],
    summary = "Gets all registered transactions",
    # description = "Returns all transactions that are registered.\n \
    # IMPORTANT: even if we are out of any transactions, meaning that they are SOLD OUT, they will be returned by this endpoint"
)
async def index(transactionService: TransactionService = Depends()):
    return await transactionService.get()


@TransactionRouter.get(
    "/{id}", 
    response_model=Transaction,
    summary = "Gets a registered tx",
    # description = "Returns the tx with the specified ID.\n \
    #     IMPORTANT: even if the tx is SOLD OUT, it will be returned"
)
async def get(id: UUID, transactionService: TransactionService = Depends()):
    return await transactionService.find(id)


@TransactionRouter.post(
    "/",
    response_model=Transaction,
    status_code=status.HTTP_201_CREATED,
    summary = "Registers a transactions"
)
async def create(
    tx: TransactionDto,
    transactionService: TransactionService = Depends(),
):
    return await transactionService.create(tx)