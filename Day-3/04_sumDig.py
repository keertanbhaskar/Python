number = int(input("Enter a number: "))
original = number
sum_digit = 0

while number > 0:

    digit = number % 10

    sum_digit += digit

    number = number // 10
print("Sum: ",sum_digit)