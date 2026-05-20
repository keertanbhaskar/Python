def calculator():
  print("Simple calculator")
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))
  operator = input("Enter operator(+, -,*, /):")
  if operator == '+':
    print("Result:",num1+num2)
  elif operator == '-':
    print('Result:',num1-num2)
  elif operator == '*':
    print('Result:',num1*num2)
  elif operator == '/':
    if num2 != 0:
      print('Result:',num1/num2)
    else:
      print("Cannot divided by zero")
  else:
    print("Invalid operator.")

calculator()

  