# Errors
'''
3 types of error
=> syntax error
=> runtime Error/Exception
=> logical error
'''

# try-except
try:
    num = int(input("Enter a number: "))
    result = 10/num
    print("Result:",result)

except ZeroDivisionError:
    print("you cannot divide by zero!")

except ValueError:
    print("Please enter a valid number.")

# Multiple errors
try:
    num = int(input("Enter a number: "))
    result = 10/num
    print("Result:",result)

except (ValueError, ZeroDivisionError):
    print("Error occurs")


# general errors
try:
    x = int("hey")
except Exception as e:
    print("something went wrong",e)


# finally
try:
    file = open("data.txt","r")
    print(file.read())
except FileNotFoundError:
    print("file not found.")
finally:
    print("End of program")

# else with try
try:
    x = 10/2
    print(x)
except ZeroDivisionError:
    print("Error")
else:
    print("No error happened")


# creating our own error types
age = -5
if age > 0:
    raise ValueError("Age cannot be negative")

# Ex = ATM Balance => dataType Integer

    
balance = 500
withDraw = 1000
if withDraw > balance:
    raise ValueError("Insufficient balance")


# Type error  => wrong datatype
name = 123
if not isinstance(name,str):
    raise TypeError("Name must in string")

# Index Error
li = [10,20,30]

index = 5

if index >= len(li):
    raise IndexError("Index out of range")