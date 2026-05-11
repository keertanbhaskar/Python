string = input("Enter String: ")
# way 1
rev = string[::-1]
print("reversed string 1 :",rev)

# way 2
revString = ""
for c in string:
  revString = c + revString 
print("reversed string 2 :",revString)