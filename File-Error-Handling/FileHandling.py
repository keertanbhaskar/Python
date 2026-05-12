# Open() => requires file-path and mode as arguments.
# file = open("file.md","r")
# content = file.read()
# print(content)
# file.close()

# with open => file closes automatically , safer n cleaner
# with open("file.md",'r') as file:
#   content = file.read()
#   print(content)

# ---- reading line by line --------
with open('file.md','r') as file:
  lines = file.readlines()
print(lines)