from collections import Counter

list_num = list(map(int,input("Enter list values with space").split()))

count = Counter(list_num)
print(count)