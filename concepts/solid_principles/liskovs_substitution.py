# Liskov's Substitution Principle: Objects of the parent class should be replaceable by objects of subclass
# without breaking the code.
from abc import abstractmethod


# Incorrect: Penguin cannot fly. When fly method runs on penguin, it will fail
class BirdIncorrect:
    def __init__(self):
        pass

    @abstractmethod
    def fly(self):
        raise Exception("Fly method not implemented in the base class")


class EagleIncorrect(BirdIncorrect):
    def __init__(self):
        super().__init__()
        pass

    def fly(self):
        print("Eagle flies")


class PenguinIncorrect(BirdIncorrect):
    def __init__(self):
        super().__init__()
        pass

    def fly(self):
        raise Exception("Penguin does not fly")


def incorrect_fly():
    bird_arr: list[BirdIncorrect] = [EagleIncorrect(), PenguinIncorrect()]
    for b in bird_arr:
        b.fly()  # this will fail in case of penguin


# Correct: Implement the same method but a bit differently.

class Bird:
    def __init__(self):
        pass

    @abstractmethod
    def move(self):
        raise Exception("Move method not implemented in the base class")


class Eagle(Bird):
    def __init__(self):
        super().__init__()
        pass

    def move(self):
        self.fly()

    def fly(self):
        print("Eagle flies.")


class Penguin(Bird):
    def __init__(self):
        super().__init__()
        pass

    def walk(self):
        raise Exception("Penguin walks.")

    def move(self):
        self.walk()


def correct_move():
    bird_arr: list[Bird] = [Eagle(), Penguin()]
    for b in bird_arr:
        b.move()  # this will work for both.
