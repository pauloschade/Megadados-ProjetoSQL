from infrastructure.database import create_all, get_db
from domain.Product import ProductModel
from domain.Stock import StockModel
from domain.Transaction import TransactionModel
import uuid

db = get_db()
create_all()
db.commit()


product_01 = ProductModel(id= uuid.uuid4(), name="produto1", price=10)
product_02 = ProductModel(id= uuid.uuid4(), name="produto2", price=20)
product_03 = ProductModel(id= uuid.uuid4(), name="produto3", price=30)

db.add(product_01)
db.add(product_02)
db.add(product_03)

db.commit()