# The Fibonacci sequence is a type series where 
# each number is the sum of the two that precede it

number = int(input("Enter a number: "))
def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1)+fibonacci(n-2)
  
fib = fibonacci(number)
print(fib)
