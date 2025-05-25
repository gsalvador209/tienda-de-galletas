from sqlalchemy import Column, Integer, ForeignKey, DECIMAL
from . import Base
from sqlalchemy.orm import relationship

class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(DECIMAL(10,2), nullable=False)

    order = relationship("Order", back_populates="items")
    product = relationship("Product")
