from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum


class OrderStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


class OrderBase(BaseModel):
    user_id: int
    product_name: str
    quantity: int
    price: float


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    product_name: Optional[str] = None
    quantity: Optional[int] = None
    price: Optional[float] = None
    status: Optional[OrderStatus] = None


class Order(OrderBase):
    id: int
    status: OrderStatus
    total_amount: float
    created_at: datetime

    class Config:
        from_attributes = True
