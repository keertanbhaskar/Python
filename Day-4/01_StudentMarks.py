student_marks = {
  "keerti":89,
  "shama":90,
  "Krishna":80,
  "Megha":78
}

print(student_marks)

# access values
print(student_marks["keerti"])

# add new students
student_marks["ravi"] = 88

# update marks
student_marks["keerti"] = 98

# delete student
del student_marks["shama"]

# loop 
for student,marks in student_marks.items():
  print(student,":",marks)

# take input from user

Student_Marks = {}
n = int(input("Enter many Students:"))
for i in range(n):
  name = input("Enter student name:")
  marks = int(input("Enter marks:"))
  Student_Marks[name] = marks
print(Student_Marks)