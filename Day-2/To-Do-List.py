List = []
while True:
  choice = input("Choose the Option: ")
  if choice == "1":
    add = input("Enter task:")
    List.append(add)
  elif choice == "2":
    List.pop()
  elif choice == "3":
    print(List)
  elif choice == "4":
    exit()

    
