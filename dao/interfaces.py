from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any


# SOLID: Interface Segregation Principle (ISP)
# Separate interfaces for different operations
class BaseRepository(ABC):
    @abstractmethod
    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[Dict[str, Any]]:
        pass

    @abstractmethod
    def get_all(self) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def update(self, id: int, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        pass

    @abstractmethod
    def delete(self, id: int) -> bool:
        pass
