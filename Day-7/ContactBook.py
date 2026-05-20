import csv
def add_contact():
  name = input("Name: ")
  phone = input("phone: ")
  with open('contacts.csv','a',newline='') as file:
    writer = csv.writer(file)
    writer.writerow([name,phone])
  print('Contact Saved.')

def show_contacts():
  with open('contacts.csv','r') as file:
    reader = csv.reader(file)
    print("Your Contacts")
    for row in reader:
      print(f'Name:{row[0]},Phone:{row[1]}')

add_contact()
show_contacts()
    