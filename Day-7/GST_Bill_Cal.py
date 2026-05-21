# GST BILL CALCULATOR
price = float(input("Enter item price: "))
gstRate = float(input("Enter GST rate (%): "))

def gstCalculator(price,gstRate):
  gstAmount = (price * gstRate)/100
  finalBill = price + gstAmount

  print('Gst amount :',gstAmount)
  print('TotalBill:',finalBill)

gstCalculator(price,gstRate)