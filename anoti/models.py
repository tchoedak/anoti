from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Boolean,
    Float
)
Base = declarative_base()


class Order(object):
    __tablename__ = 'orders'

    amazon_order_id = Column(Integer, primary_key=True)
    is_prime = Column(Boolean)
    item = Column(String)
    price = Column(Float)
    purchase_date = Column(DateTime)
    order_status = Column(String)
    order_type = Column(String)
    ship_service_level = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

