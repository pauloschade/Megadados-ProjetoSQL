from typing import List
import uuid
from fastapi import Depends, HTTPException
from domain.Transaction import Transaction, TransactionDto
from repositories.TransactionRepository import TransactionRepository


class TransactionService:

    def __init__(
        self, transactionRepository: TransactionRepository = Depends()
    ) -> None:
        self.transactionRepository = transactionRepository

    async def get(self) -> List[Transaction]:
        return await self.transactionRepository.get()

    async def find(self, id: uuid.UUID) -> Transaction:
        return await self.transactionRepository.find(id)

    async def create(self, tx: TransactionDto) -> Transaction:
        try:
            new_tx = self.generate_tx(tx)
            created_tx = await self.transactionRepository.create(new_tx)
            self.transactionRepository.commit()
            return created_tx
        except:
            self.transactionRepository.rollback()
            raise HTTPException(status_code=400, detail=f"stock {tx.stock_id} doesn't have enough supply (removing {-1 * tx.quantity} exceded the limit)")


    def generate_tx(self, tx: TransactionDto):
        return Transaction(
            stock_id = tx.stock_id,
            quantity = tx.quantity
        )
