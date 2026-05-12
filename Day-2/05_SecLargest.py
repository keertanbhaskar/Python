list_num = list(map(int,input("Enter list values with space").split()))

max_num = list_num[0]
sec_largest = list_num[0]

for i in list_num:
  if i > max_num:
    sec_largest = max_num
    max_num = i
  elif i > sec_largest and i != max_num:
    sec_largest = i
print("max:",max_num)
print("Second largest:",sec_largest)
