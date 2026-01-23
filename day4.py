# abstraction

from abc import ABC, abstractmethod

class Sensor(ABC):

    @abstractmethod
    def detect(self):
        pass

class Motionsensor(Sensor):
    def detect(self):
        print("motion detected")

class Watersensor(Sensor):
    def detect(self):
        print("water leakage detected")

if __name__ == "__main__":
    s = Motionsensor()
    u = Watersensor()
    s.detect()
    u.detect()




class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass

class Email(Notification):
    def send(self, message):
        print(f"email sent! : {message}")

class SMS(Notification):
    def send(self, message):
        print(f"sms sent! : {message}")

if __name__ == "__main__":
    a = Email()
    s = SMS()
    a.send("your otp is 123")
    s.send("pls recharge ur num")



# vehicle
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("car engine started!")

class Bike(Vehicle):
    def start(self):
        print("bike engine started!")


if __name__ == "__main__":
    z = Car()
    a = Bike()
    z.start()
    a.start()