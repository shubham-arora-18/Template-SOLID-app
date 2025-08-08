# Single Responsibility Principle: States that a class should have only one reason to change.
# Meaning it should only have one responsibility.

# Incorrect: Tries to handle multiple things

class User:
    def __init__(self):
        pass

    def create_new_user(self):
        # business logic to create new user
        pass

    def save_user_in_db(self):
        # saves the user object to db
        pass


# Correct: Different classes handling different things

class UserService:
    def __init__(self):
        pass

    def create_new_user(self):
        # business logic to create new user
        pass


class UserDAO:
    def __init__(self):
        pass

    def save_user_in_db(self):
        # saves the user object to db
        pass
