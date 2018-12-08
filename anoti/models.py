from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float


Base = declarative_base()


class AmazonOrder(Base):
    __tablename__ = 'amazon_orders'

    amazon_order_id = Column(String, primary_key=True)
    is_prime = Column(Boolean)
    title = Column(String)
    number_of_items = Column(Integer)
    price = Column(Float)
    purchase_date = Column(DateTime)
    order_status = Column(String)
    order_type = Column(String)
    ship_service_level = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
