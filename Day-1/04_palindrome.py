Check = input("Enter value to check palindrome: ")

# only works on strings
reverse = Check[::-1]

if Check == reverse:
  print(f"{Check} is palidrome")
else:
  print(f" {Check} is not a palindrome")


# 2nd way for numbers 
number = int(input("Enter a number: "))

rev = 0
real_num = number
while number > 0:
  last_dig = number % 10
  rev = rev * 10 + last_dig
  number = number // 10
if real_num == rev:
  print(f"{real_num} is palindrome")
else:
  print(f"{real_num} is not a palindrome")


