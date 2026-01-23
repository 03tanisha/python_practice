# polymorphism

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

# child class
class Dog(Animal):
    def speak(self):
        print("dark barks")

class Cat(Animal):
    def speak(self):
        print("cat does meowwwwwww!")

s = [Dog(), Cat()]

if __name__ == "__main__":
    for a in s :
        a.speak()


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rec(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


if __name__ == "__main__":
    c = [Rec(2,4), Circle(4)]
    for a in c:
        print(a.area())



