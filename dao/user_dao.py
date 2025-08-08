from dao.interfaces import BaseRepository
from typing import List, Optional, Dict, Any
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class UserDAO(BaseRepository):
    cls_next_id = 1
    cls_user_dict = {}
    """
    SOLID: Single Responsibility Principle (SRP)
    - Only responsible for user data access operations
    """

    def __init__(self):
        logger.info("init method for user dao")
        self._users: Dict[int, Dict[str, Any]] = UserDAO.cls_user_dict

    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        user_data = {
            "id": UserDAO.cls_next_id,
            "name": data["name"],
            "email": data["email"],
            "created_at": datetime.now()
        }
        self._users[UserDAO.cls_next_id] = user_data
        UserDAO.cls_next_id += 1
        return user_data

    def get_by_id(self, id: int) -> Optional[Dict[str, Any]]:
        return self._users.get(id)

    def get_all(self) -> List[Dict[str, Any]]:
        return list(self._users.values())

    def update(self, id: int, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        if id not in self._users:
            return None

        user = self._users[id]
        for key, value in data.items():
            if value is not None and key in ["name", "email"]:
                user[key] = value

        return user

    def delete(self, id: int) -> bool:
        if id in self._users:
            del self._users[id]
            return True
        return False

    def get_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        for user in self._users.values():
            if user["email"] == email:
                return user
        return None
