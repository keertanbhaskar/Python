number = int(input("Enter a number: "))
def fact(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return n*fact(n-1)

factorial = fact(number)
print(factorial)