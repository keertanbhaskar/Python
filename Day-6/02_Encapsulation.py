# Encapsulation => wrapping data and methods together in one class and 
# restricting direct access to data
# access specifier => public, protected, private

# example => private
class BankAccount:
  def __init__(self,balance):
    self.__balance =balance  

  def deposit(self,amount):
    self.__balance += amount
  
  def show_balance(self):
    print(self.__balance)

acc = BankAccount(1500)
acc.deposit(500)
acc.show_balance()

# print(acc._BankAccount__balance) => dont use
# protected => accessible within cls and its subcls
class Employee:
  def __init__(self,name,age):
    self._name = name #protected
    self.age = age
class SubEmployee(Employee):
  def show_name(self):
    print("Name:",self._name) 

emp = SubEmployee("KK",23)
print(emp._name)
emp.show_name()

# getter and setter method
# getter and setter methods are used to access and modify private attributes safely.

class Emp:
  def __init__(self):
    self.__salary = 5000
  
  def get_salary(self):    # Getter method
        return self.__salary
  
  def set_salary(self,amount):
    if amount > 0:
      self.__salary = amount
    else:
      print("Invalid salary amount!")

e1 = Emp()
print(e1.get_salary())

e1.set_salary(7000)
print(e1.get_salary())