# classes and objects
'''
oop => object-oriented programming
A class defines what an object should look like, 
and an object is created based on that class.
'''

# basic syntax to create cls and obj
'''
class Student:
  name = "keertana"
  age = 20
# object
s1 = Student()
print(s1.name)
print(s1.age)
'''

'''
# methods in class
class Person():
  def study(self):
    print("person is undergraduate")
p1 = Person()
p1.study()

'''

# self => current object

# constructor(__init__) => we need it because to initialize the object data
'''
class Student1:
  def __init__(self):
    print("Constructor called")
s2 = Student1()
'''
'''
class Student:
  def __init__(self,name,age):
    self.name = name
    self.age = age
s1 = Student("Keerti",20)
print(f"my name is {s1.name} and i'm {s1.age}yrs old")
'''

# instance variables and class variables
# 1.instance variables diff for every object
# 2.class var shared by all objects
class Student:
  school = "AIET college"  #cls var
  def __init__(self,name):
    self.name = name #instance var

s1 = Student("keerti") 
s2 = Student("Sam")

print(s1.school)
print(s2.school)
