from domain.base.UUIDBase import UUIDBaseModel
from sqlalchemy.schema import Column
from sqlalchemy import String, Integer, ForeignKey
from infrastructure.database import Base

class TransactionModel(UUIDBaseModel, Base):

    __tablename__ = "Transaction"
    stock_id = Column(String(50), ForeignKey("Stock.id"), nullable=False)
    quantity = Column(Integer)