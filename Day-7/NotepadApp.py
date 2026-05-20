def write_note():
  note = input("Write your note:")
  with open("notes.txt",'a') as f:
    f.write(note+"\n")

def read_notes():
  print("Your Notes:")
  with open("notes.txt",'r') as f:
    for line in f:
      print('-',line.strip())

write_note()
read_notes()