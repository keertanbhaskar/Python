number = int(input("Enter a number: "))

if number <= 1:
  print("Not Prime")
else:
  for i in range(2, number):
    if number % i == 0:
      print("Not Prime")
      break
  else:
    print(f"{number} is prime")

'''
for-else

The else runs ONLY if loop finishes normally.

If loop breaks:

else will NOT run.
'''