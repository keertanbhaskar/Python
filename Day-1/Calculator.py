while True:
  choice = input("Enter operation number: ")

  number1 = int(input("Enter number 1: "))
  number2 = int(input("Enter number 2: "))

  match choice:
    case "1":
      print(number1 + number2)
    case "2":
      print(number1 - number2)
    case "3":
      print(number1 * number2)
    case "4":
      if number2 != 0:
        print(number1 / number2)
      else:
        print("Cannot divide by zero")
    case _:
      print("Invalid operation")


