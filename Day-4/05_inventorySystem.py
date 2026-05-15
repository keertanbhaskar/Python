inventory_system = {}

while True:
  choice = int(input("Enter Choice:"))
  if choice == 1:
    prd_key = input("Enter key:")
    prd_val = input("Enter Value:")
    inventory_system[prd_key] = prd_val
    print("Product added")

  elif choice == 2:
    print("\nInventory Items:")
    for prd_key,prd_val in inventory_system.items():
      print(prd_key,":",prd_val)

  elif choice == "3":

      product = input("Enter product name: ")

      if product in inventory_system:

          new_quantity = int(input("Enter new quantity: "))
          inventory_system[product] = new_quantity

          print("Updated successfully")

      else:
          print("Product not found")

  elif choice == 4:
    product = input("Enter product:")
    if product in inventory_system:
      del inventory_system[product]
    else:
      product("product not found")
  elif choice == 5:
     print("Exiting...")
     exit()
  else:
     print("invalid choice")
      

    
