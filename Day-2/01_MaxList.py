# Find max from list

# taking list as input from user
'''
The split() method separates input based on spaces 
and returns a list.

Flow:

input() → gets string
.split() → creates list of strings
map(int, ...) → converts each string to integer
list(...) → converts map object into list
'''

li =list(map(int, input("Enter elements separated by space: ").split()))
print("List:",li)
print(type(li))
max_num = max(li)
print("Max ix:",max_num)


max_number = li[0]
for i in li:
  if i > max_number:
    max_number = i
print("Max:",max_number)

