list_value = [1,3,6,1,6,7,8,9]
unique  = []
occurred = []

for i in list_value:
  if list_value.count(i) == 1:
    unique.append(i)
  else:
    occurred.append(i)

print(f"unique values : {unique} \n occurred values:{occurred}")