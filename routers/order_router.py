from fastapi import APIRouter, Depends
from typing import List
from models.order import Order, OrderCreate, OrderUpdate
from services.order_service import OrderService
from dao.order_dao import OrderDAO
from dao.user_dao import UserDAO

order_router = APIRouter(prefix="/orders", tags=["orders"])


# Dependency injection following DIP
def get_order_dao():
    return OrderDAO()


def get_user_dao():
    return UserDAO()


def get_order_service(
        order_dao: OrderDAO = Depends(get_order_dao),
        user_dao: UserDAO = Depends(get_user_dao)
):
    return OrderService(order_dao, user_dao)


@order_router.post("/", response_model=Order)
def create_order(order: OrderCreate, service: OrderService = Depends(get_order_service)):
    """
    SOLID: Open/Closed Principle (OCP)
    - Router is open for extension (new endpoints) but closed for modification
    """
    return service.create_order(order)


@order_router.get("/{order_id}", response_model=Order)
def get_order(order_id: int, service: OrderService = Depends(get_order_service)):
    return service.get_order(order_id)


@order_router.get("/", response_model=List[Order])
def get_all_orders(service: OrderService = Depends(get_order_service)):
    return service.get_all_orders()


@order_router.get("/user/{user_id}", response_model=List[Order])
def get_user_orders(user_id: int, service: OrderService = Depends(get_order_service)):
    return service.get_user_orders(user_id)


@order_router.put("/{order_id}", response_model=Order)
def update_order(order_id: int, order: OrderUpdate, service: OrderService = Depends(get_order_service)):
    return service.update_order(order_id, order)


@order_router.delete("/{order_id}")
def delete_order(order_id: int, service: OrderService = Depends(get_order_service)):
    success = service.delete_order(order_id)
    return {"message": "Order deleted successfully" if success else "Failed to delete order"}
