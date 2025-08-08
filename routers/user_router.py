from fastapi import APIRouter, Depends
from typing import List
from models.user import User, UserCreate, UserUpdate
from services.user_service import UserService
from dao.user_dao import UserDAO

user_router = APIRouter(prefix="/users", tags=["users"])


# Dependency injection following DIP
def get_user_dao():
    return UserDAO()


def get_user_service(user_dao: UserDAO = Depends(get_user_dao)):
    return UserService(user_dao)


@user_router.post("/", response_model=User)
def create_user(user: UserCreate, service: UserService = Depends(get_user_service)):
    """
    SOLID: Open/Closed Principle (OCP)
    - Router is open for extension (new endpoints) but closed for modification
    """
    return service.create_user(user)


@user_router.get("/{user_id}", response_model=User)
def get_user(user_id: int, service: UserService = Depends(get_user_service)):
    return service.get_user(user_id)


@user_router.get("/", response_model=List[User])
def get_all_users(service: UserService = Depends(get_user_service)):
    return service.get_all_users()


@user_router.put("/{user_id}", response_model=User)
def update_user(user_id: int, user: UserUpdate, service: UserService = Depends(get_user_service)):
    return service.update_user(user_id, user)


@user_router.delete("/{user_id}")
def delete_user(user_id: int, service: UserService = Depends(get_user_service)):
    success = service.delete_user(user_id)
    return {"message": "User deleted successfully" if success else "Failed to delete user"}
