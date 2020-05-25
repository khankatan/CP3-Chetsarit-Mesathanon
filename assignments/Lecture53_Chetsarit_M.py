def vatCal(price,taxrate):
    amount = price*(1+(taxrate/100))
    return amount

print("========== VAT CALCULATION ==========")
priceInput = int(input("Product price (THB) : "))
taxrateInput = int(input("Tex rate (%) : "))
print("Price includes tax :", vatCal(priceInput,taxrateInput))
print("========== =============== ==========")