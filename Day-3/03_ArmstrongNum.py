number = int(input("Enter a number: "))

original = number

count = len(str(number))
sum_digit = 0

while number > 0:

    digit = number % 10

    sum_digit += digit ** count

    number = number // 10

if sum_digit == original:
    print(f"{original} is an Armstrong number")

else:
    print(f"{original} is not an Armstrong number")