# services/user_service.py
from dao.interfaces import BaseRepository
from models.user import User, UserCreate, UserUpdate
from typing import List, Optional
from fastapi import HTTPException


class UserService:
    """
    SOLID: Dependency Inversion Principle (DIP)
    - Depends on abstraction (BaseRepository) not concrete implementation

    SOLID: Single Responsibility Principle (SRP)
    - Only responsible for user business logic
    """

    def __init__(self, user_dao: BaseRepository):
        self.user_dao = user_dao

    def create_user(self, user_data: UserCreate) -> User:
        # Business logic: Check if email already exists
        if hasattr(self.user_dao, 'get_by_email'):
            existing_user = self.user_dao.get_by_email(user_data.email)
            if existing_user:
                raise HTTPException(status_code=400, detail="Email already registered")

        user_dict = self.user_dao.create(user_data.model_dump())
        return User(**user_dict)

    def get_user(self, user_id: int) -> User:
        user_dict = self.user_dao.get_by_id(user_id)
        if not user_dict:
            raise HTTPException(status_code=404, detail="User not found")
        return User(**user_dict)

    def get_all_users(self) -> List[User]:
        users_dict = self.user_dao.get_all()
        return [User(**user) for user in users_dict]

    def update_user(self, user_id: int, user_data: UserUpdate) -> User:
        # Business logic: Check if user exists
        existing_user = self.user_dao.get_by_id(user_id)
        if not existing_user:
            raise HTTPException(status_code=404, detail="User not found")

        # Business logic: Check email uniqueness if email is being updated
        if user_data.email and hasattr(self.user_dao, 'get_by_email'):
            email_user = self.user_dao.get_by_email(user_data.email)
            if email_user and email_user["id"] != user_id:
                raise HTTPException(status_code=400, detail="Email already in use")

        updated_user = self.user_dao.update(user_id, user_data.model_dump(exclude_unset=True))
        return User(**updated_user)

    def delete_user(self, user_id: int) -> bool:
        if not self.user_dao.get_by_id(user_id):
            raise HTTPException(status_code=404, detail="User not found")

        return self.user_dao.delete(user_id)