# Interface Segregation Principle: States that a class should not implement an Inteface if all of the methods in the
# interface does not make sense for the class. Instead the interface should be broken down further.

# Incorrect: Robot class forced to implement the eat method.

from abc import abstractmethod


class Worker:
    @abstractmethod
    def work(self):
        raise Exception("Worker class does not implement work method.")

    @abstractmethod
    def eat(self):
        raise Exception("Worker class does not implement eat method.")


class HumanIncorrect(Worker):
    def work(self):
        print("Human works")

    def eat(self):
        print("Human eats")


class RobotIncorrect(Worker):
    def work(self):
        print("Robot works")

    def eat(self):
        raise Exception("Robot does not eat")


# Correct: Breaking down the interface into 2:

class Workable:
    @abstractmethod
    def work(self):
        raise Exception("Workable class does not implement work method.")


class Eatable:
    @abstractmethod
    def eat(self):
        raise Exception("Eatable class does not implement eat method.")


class Human(Workable, Eatable):
    def work(self):
        print("Human works")

    def eat(self):
        print("Human eats")


class Robot(Workable):
    def work(self):
        print("Robot works")
