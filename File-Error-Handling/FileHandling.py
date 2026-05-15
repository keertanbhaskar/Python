# Open() => requires file-path and mode as arguments.
# read the whole text as string.


# file = open("file.md","r")
# content = file.read()
# print(content)
# file.close()

# with open => file closes automatically , safer n cleaner 

with open("file.md",'r') as file:
  content = file.read()
  print(content)



#number of characters we want to read,
'''
file = open("file.md","r")
content = file.read(30)
print(type(content))
print(content)
file.close()
'''

# readline() in Python is used to read one line at a time from a file.
'''
file = open("file.md","r")
line1 = file.readline()
print(line1)
line2 = file.readline()
print(line2)
file.close()  
'''


# readlines()
'''
file = open("textFile.txt","r")
line = file.readlines()
print(line)
file.close() 
'''
# another way to read lines

'''
file = open("textFile.txt","r")
content = file.read().splitlines()
# line = content.splitlines()
# print(line)
print(content)
file.close()
'''

# ======== write and append ======
'''
with open("file2.txt","w") as f1:
  f1.write("hello, how are you")

# overwrite the file
with open("file2.txt","w") as f1:
  f1.write("hello, how was the day")

# append
with open("textFile1.txt","a") as f:
  f.write("\nhey, good morning")

# r+ => read + write without deleting
with open("file2.txt","r+") as f:
  f.write("hey")

# control position = > seek
with open("file2.txt","r+") as f:
  f.seek(6)
  f.write("bad")
'''

# delete files => can use remove or unlink
'''
import os
file_name = "file3.txt"
os.remove(file_name)
# os.unlink(file_name)
print("File deleted")

# can give error if file not exist
import os

if os.path.exists("data.txt"):
    os.remove("data.txt")
    print("Deleted")
else:
    print("File not found")

# delete the empty folder
os.rmdir("folder_name")

# Delete Folder With Files
import shutil
shutil.rmtree("folder_name")

# copy file
shutil.copy("textFile.txt", "text2.txt")

# Move file
shutil.move("textFile1.txt", "Day-1/")

'''
# =========== Handling different types of files ===============
'''
# basic file reading
with open("user.csv","r") as f:
  content = f.read()
print(content)
'''
'''
import csv
with open("user.csv") as f:
  reader = csv.reader(f)

  for row in reader:
    print(row)
'''

'''
with open("user.csv", "w") as file:
    file.write("John,21\n")
    file.write("John,21\n")
    file.write("John,21\n")
'''



