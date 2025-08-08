# Dependency Inversion Principle: States that the high level modules should not depend on the low level modules
# rather both should depend on abstraction/interface.
from abc import abstractmethod


# Incorrect: Service Object Directly depends on the DAO object

class UserDAOIncorrect:
    def save_user(self):
        print("User saved to db")


class UserServiceIncorrect:
    def __init__(self, user_dao: UserDAOIncorrect):
        self.user_dao = user_dao

    def create_user(self):
        # business logic
        self.user_dao.save_user()


# Correct: Service Object Depends on DAO Interface and UserDAO extends from DAO Interface.

class DAO:
    @abstractmethod
    def create_entity(self):
        raise Exception("create_entity method not implemented in DAO class.")


class UserDAO(DAO):
    def create_entity(self):
        print("User saved to db")


class UserService:
    def __init__(self, user_dao: DAO):
        self.user_dao = user_dao

    def create_user(self):
        # business logic
        self.user_dao.create_entity()
