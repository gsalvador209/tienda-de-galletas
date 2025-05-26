from sqlalchemy import Column, Integer, ForeignKey, Enum, DECIMAL, VARCHAR, TIMESTAMP
from . import Base
from sqlalchemy.orm import relationship
import enum

class OrderStatus(enum.Enum):
    pendiente = "pendiente"
    enviado = "enviado"
    completado = "completado"

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(Enum(OrderStatus), default=OrderStatus.pendiente)
    total = Column(DECIMAL(10,2), nullable=False)
    direction = Column(VARCHAR(255))
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
    updated_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")

    user = relationship("User", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")
