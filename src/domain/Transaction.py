from domain.base.UUIDBase import UUIDBase, UUIDBaseModel
from sqlalchemy.schema import Column
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from pydantic import Field, BaseModel
import uuid as uuid_pkg
from infrastructure.database import Base

class Transaction(UUIDBase):

    """
    Class for transaction in stock
    """
    stock_id : uuid_pkg.UUID = Field(
        title = 'stock referrenced'
    )

    quantity : int = Field(
        title = 'quantity being added/removed from stock'
    )
    class Config:
        orm_mode = True

class TransactionDto(BaseModel):

    """
    Class for creating transactions
    """
    stock_id : uuid_pkg.UUID = Field(
        title = 'stock referrenced'
    )

    quantity : int = Field(
        title = 'quantity being added/removed from stock'
    )

class TransactionModel(UUIDBaseModel, Base):

    __tablename__ = "Transaction"
    stock_id = Column(String(50), ForeignKey("Stock.id", ondelete='CASCADE'), nullable=False)
    quantity = Column(Integer)

    Stock = relationship("StockModel", backref=backref("TransactionModel", cascade="all,delete"))