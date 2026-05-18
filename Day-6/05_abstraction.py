# Hiding internal implementation details and showing only essential functionality.
from abc import ABC,abstractmethod
class Vehicle(ABC):
  
  @abstractmethod
  def go(self):
    pass
  @abstractmethod
  def stop(self):
    pass

class Car(Vehicle):
   def go(self):
    print("drive the car")

   def stop(self):
    print("Stop the car")

class Bike(Vehicle):
  def go(self):
    print("drive the bike")

  def stop(self):
    print("Stop the bike")     

car = Car()
car.go()
car.stop()

bike = Bike()
bike.go()
bike.stop()

class Boat(Vehicle):
  def go(self):
    print("you sail the boat")

boat = Boat()    