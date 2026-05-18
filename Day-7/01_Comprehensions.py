labels = [f'Apple #{i}' for i in range(1,6)]
print(labels)

# square numbers
numbers = [1,2,3,4]
square = [i**2 for i in numbers]
print(square)

# filtering even numbers
nums = [1,2,7,4,9,8]
even = [x for x in nums if x % 2 == 0]
print(even)

# Dictionary Comprehensions
students = ["Riya", "Aman", "Priya"]
length_map = {name:len(name) for name in students}
print(length_map)

# Lambda Functions – Anonymous Functions (function without a name)
sq = lambda x : x*x
print(sq(5))

# Multiple Arguments
add = lambda a,b:a+b
print(add(3,6))

# map => applies function to every elements
num = [1,2,6,7]
squ = list(map(lambda x:x*x,num))
print(squ)

# filter => Filters elements based on condition.
even1 = list(filter(lambda x: x % 2 == 0, nums))

print(even1)

# sorting
students = [("Riya", 88), ("Aman", 75), ("Dev", 92)]
students.sort(key=lambda x: x[1], reverse=True)
print(students)