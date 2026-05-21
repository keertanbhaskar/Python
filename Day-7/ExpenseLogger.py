import csv
with open('expenseLog.csv','w',newline='') as file:
  writer = csv.writer(file)

  writer.writerow(['Date',"Amount","Category"])

  n = int(input("how many expenses do you want to enter: "))

  for i in range(n):
    print(f"==========Expense{i+1}==========")
    date = input("Enter date (dd/mm/yyyy): ")
    amount = input("Enter amount: ")
    category = input("Enter category: ")

    writer.writerow([date,amount,category])


with open("expenseLog.csv", "r") as file:
    reader = csv.reader(file)

    print('==========Expense=======')
    for row in reader:
        print(row)
    