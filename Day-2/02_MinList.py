list_num = list(map(int,input("Enter your numbers with space: ").split()))

min_num = list_num[0]

for i in list_num:
  if i < min_num:
    min_num = i
print("Min:",min_num)

min_number = min(list_num)
print("Minimum:",min_number)