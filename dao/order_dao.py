from dao.interfaces import BaseRepository
from typing import List, Optional, Dict, Any
from datetime import datetime
from models.order import OrderStatus


class OrderDAO(BaseRepository):
    cls_user_dict = {}
    cls_next_id = 1
    """
    SOLID: Single Responsibility Principle (SRP)
    - Only responsible for order data access operations
    """

    def __init__(self):
        self._orders: Dict[int, Dict[str, Any]] = OrderDAO.cls_user_dict

    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        total_amount = data["quantity"] * data["price"]
        order_data = {
            "id": OrderDAO.cls_next_id,
            "user_id": data["user_id"],
            "product_name": data["product_name"],
            "quantity": data["quantity"],
            "price": data["price"],
            "total_amount": total_amount,
            "status": OrderStatus.PENDING,
            "created_at": datetime.now()
        }
        self._orders[OrderDAO.cls_next_id] = order_data
        OrderDAO.cls_next_id += 1
        return order_data

    def get_by_id(self, id: int) -> Optional[Dict[str, Any]]:
        return self._orders.get(id)

    def get_all(self) -> List[Dict[str, Any]]:
        return list(self._orders.values())

    def update(self, id: int, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        if id not in self._orders:
            return None

        order = self._orders[id]
        for key, value in data.items():
            if value is not None and key in ["product_name", "quantity", "price", "status"]:
                order[key] = value

        # Recalculate total if quantity or price changed
        if "quantity" in data or "price" in data:
            order["total_amount"] = order["quantity"] * order["price"]

        return order

    def delete(self, id: int) -> bool:
        if id in self._orders:
            del self._orders[id]
            return True
        return False

    def get_by_user_id(self, user_id: int) -> List[Dict[str, Any]]:
        return [order for order in self._orders.values() if order["user_id"] == user_id]
