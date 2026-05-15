# word count
student = {
    "Rahul": 85,
    "Anu": 92,
    "Kiran": 78
}

count = len(student)

print("Total students:", count)

# count keys
people = {
  "sar":23,
  "sam":30,
  "saj":44,
  "emily":22
}

for key in people:
  print(key,"=",len(key))

sentence = "Python is easy Python is powerful"
words = sentence.split()
word_count = {}
for word in words:
  if word in word_count:
    word_count[word] +=1
  else:
    word_count[word] = 1
print(word_count) 