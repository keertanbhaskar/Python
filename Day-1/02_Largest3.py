num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

def largest(n1,n2,n3):
  if n1 > n2 and n1 > n3:
    return f"{n1} is largest"
  elif n2 > n1 and n2 > n3:
    return f"{n2} is largest"
  else:
    return f"{n3} is largest"
  
largest_num = largest(num1,num2,num3)
print(largest_num)