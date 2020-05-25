def vatCal(price):
    amount = price*1.07
    return amount

print("========== VAT CALCULATION ==========")
priceInput = int(input("Product price : "))
print("Price includes tax :", vatCal(priceInput))
print("========== =============== ==========")