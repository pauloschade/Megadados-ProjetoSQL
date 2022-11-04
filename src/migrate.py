from sqlalchemy.sql import text
from infrastructure.database import create_all, get_db, engine
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

stock_01 = StockModel(id= uuid.uuid4(), product_id = product_01.id,quantity=1)
stock_02 = StockModel(id= uuid.uuid4(),  product_id = product_02.id ,quantity=2)
stock_03 = StockModel(id= uuid.uuid4(), product_id = product_03.id ,quantity=3)

db.add(product_01)
db.add(product_02)
db.add(product_03)

db.add(stock_01)
db.add(stock_02)
db.add(stock_03)

db.commit()

trigger = "CREATE TRIGGER tx_triger AFTER INSERT ON Transaction FOR EACH ROW BEGIN UPDATE Stock SET Stock.quantity = Stock.quantity + NEW.quantity WHERE Stock.id = NEW.stock_id; END;"

statement = text(trigger)

with engine.connect() as con:
    con.execute(statement)

