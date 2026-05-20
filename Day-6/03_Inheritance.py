# Inheritance
class Animal:
  def __init__(self,name):
    self.name = name
  def info(self):
    print("Animal name:",self.name)

class Dog(Animal):
  def sound(self):
    print(self.name,"barks")
  
d = Dog("Buddy")
d.info()
d.sound()

# super() function is used to call methods from a superclass
class Animal1:
  def __init__(self,name):
    self.name = name

  def info(self):
    print("Animal name:",self.name)

# child class: Dog
class Dog1(Animal1):
  def __init__(self, name, breed):
    super().__init__(name)
    self.breed = breed

  def details(self):
    print(self.name,"is a",self.breed)

d1 = Dog1("Buddy","Golden Retriever")
d1.info()
d1.details()

# Single inheritance enables a derived class 
# to inherit properties from a single parent class

class Parent:
  def func1(self):
    print("this function is parent class.")
class Child(Parent):
  def fun2(self):
    print("This function is in child class.")

obj = Child()
obj.func1()
obj.fun2()    

# multiple inheritance
# a class can be derived from more than one base class
class Mother:
  motherName = ""

  def mother(self):
    print(self.motherName)
class Father:
  fatherName = ""

  def father(self):
    print(self.fatherName)

# derived class
class Son(Mother,Father):
  def parents(self):
    print("Father :",self.fatherName)
    print("Mother :",self.motherName)

s1 = Son()
s1.fatherName = "Ram"
s1.motherName = "Sita"
s1.parents()

# In multilevel inheritance, 
# features of the base class and the derived class are further inherited into the new derived class.
# Base class
class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

# Intermediate class
class Father1(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        # Call the constructor of Grandfather
        Grandfather.__init__(self, grandfathername)

# Derived class
class Son1(Father1):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        # Call the constructor of Father
        Father1.__init__(self, fathername, grandfathername)

    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print('Father name :', self.fathername)
        print('Son name :', self.sonname)

# Driver code
s1 = Son1('Prince', 'Ram', 'sham')
print(s1.grandfathername)
s1.print_name()


# Hierarchical Inheritance
# When more than one derived class are created from a single base
# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")

# Derived class 1
class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")

# Derived class 2
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")

# Driver code
object1 = Child1()
object2 = Child2()

object1.func1()
object1.func2()
object2.func1()
object2.func3()



