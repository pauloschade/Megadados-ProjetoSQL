from fastapi import HTTPException, Depends
from typing import List
from uuid import UUID
from sqlalchemy.orm import Session
from domain.Transaction import Transaction, TransactionDto, TransactionModel
from infrastructure.database import get_db_connection

class TransactionRepository:

    db : Session

    def __init__(self, db: Session = Depends(get_db_connection)):
        self.db = db

    async def get(self) -> List[Transaction]:
        return self.db.query(TransactionModel).all()

    async def find(self, id: UUID) -> Transaction:
        tx = self.db.query(TransactionModel).filter(TransactionModel.id == str(id)).first()
        if tx is None:
            raise HTTPException(status_code=404, detail="Transaction not found")
        return tx
       

    async def create(self, tx: Transaction) -> Transaction:
        tx_model = TransactionModel(id = str(tx.id), stock_id = tx.stock_id, quantity = tx.quantity)
        self.db.add(tx_model)
        return tx_model

    def commit(self):
        return self.db.commit()
        
    def rollback(self):
        return self.db.rollback()