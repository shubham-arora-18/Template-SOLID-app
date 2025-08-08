from dao.interfaces import BaseRepository
from models.order import Order, OrderCreate, OrderUpdate
from typing import List, Optional
from fastapi import HTTPException


class OrderService:
    """
    SOLID: Dependency Inversion Principle (DIP)
    - Depends on abstractions (BaseRepository) not concrete implementations

    SOLID: Single Responsibility Principle (SRP)
    - Only responsible for order business logic
    """

    def __init__(self, order_dao: BaseRepository, user_dao: BaseRepository):
        self.order_dao = order_dao
        self.user_dao = user_dao

    def create_order(self, order_data: OrderCreate) -> Order:
        # Business logic: Validate user exists
        user = self.user_dao.get_by_id(order_data.user_id)
        if not user:
            raise HTTPException(status_code=400, detail="User not found")

        # Business logic: Validate order data
        if order_data.quantity <= 0:
            raise HTTPException(status_code=400, detail="Quantity must be positive")
        if order_data.price <= 0:
            raise HTTPException(status_code=400, detail="Price must be positive")

        order_dict = self.order_dao.create(order_data.model_dump())
        return Order(**order_dict)

    def get_order(self, order_id: int) -> Order:
        order_dict = self.order_dao.get_by_id(order_id)
        if not order_dict:
            raise HTTPException(status_code=404, detail="Order not found")
        return Order(**order_dict)

    def get_all_orders(self) -> List[Order]:
        orders_dict = self.order_dao.get_all()
        return [Order(**order) for order in orders_dict]

    def get_user_orders(self, user_id: int) -> List[Order]:
        # Business logic: Validate user exists
        user = self.user_dao.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        if hasattr(self.order_dao, 'get_by_user_id'):
            orders_dict = self.order_dao.get_by_user_id(user_id)
        else:
            # Fallback if method doesn't exist
            all_orders = self.order_dao.get_all()
            orders_dict = [order for order in all_orders if order["user_id"] == user_id]

        return [Order(**order) for order in orders_dict]

    def update_order(self, order_id: int, order_data: OrderUpdate) -> Order:
        # Business logic: Check if order exists
        existing_order = self.order_dao.get_by_id(order_id)
        if not existing_order:
            raise HTTPException(status_code=404, detail="Order not found")

        # Business logic: Validate updated data
        if order_data.quantity is not None and order_data.quantity <= 0:
            raise HTTPException(status_code=400, detail="Quantity must be positive")
        if order_data.price is not None and order_data.price <= 0:
            raise HTTPException(status_code=400, detail="Price must be positive")

        updated_order = self.order_dao.update(order_id, order_data.model_dump(exclude_unset=True))
        return Order(**updated_order)

    def delete_order(self, order_id: int) -> bool:
        if not self.order_dao.get_by_id(order_id):
            raise HTTPException(status_code=404, detail="Order not found")

        return self.order_dao.delete(order_id)
