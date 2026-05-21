# Polymorphism allows same method, function or operator to behave differently 
# depending on object it is working with.

# same method ,diff behavior
class Dog:
  def sound(self):
    print("Dog barks")
class Cat:
  def sound(self):
    print("Cat meows")

d = Dog()
c = Cat()

d.sound()
c.sound()







# method overriding (compile-time polymorphism)

class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()


# Same method name with different arguments.
# method overloading
class Calculator:

    def add(self, a, b=0, c=0,*args):
      total = a + b + c + sum(args)
      print(total)

c = Calculator()

c.add(5)
c.add(5, 10)
c.add(5, 10, 15,2,7)