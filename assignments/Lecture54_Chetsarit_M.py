def login():
    print("========== L O N G I N ==========")
    user1 = input("USERNAME : ")
    pass1 = input("PASSWORD : ")
    while user1 != "admin" or pass1 != "1234":
        print("---------- ----------- ----------")
        print("USERNAME OR PASSWORD INCORRECT!!")
        print("PLEASE ENTER AGAIN")
        user1 = input("USERNAME : ")
        pass1 = input("PASSWORD : ")
    else:
        return
def showMenu():
    print("---------- ----------- ----------")
    print("    WELCOME TO GUPPEE DRINKS")
    print("---------- ----------- ----------")
    print("PLEASE SELECT A PRODUCT")
    print("1) COCONUT JUICE     : 100 THB")
    print("2) ORANGE JUICE      : 60  THB")
    print("3) LAMONEDE JUICE    : 80  THB")
    print("4) WATER MALON JUICE : 55  THB")
    print("---------- ----------- ----------")
def producePrice(productInput):
    if productInput == str(1):
        return 100
    elif productInput == str(2):
        return 60
    elif productInput == str(3):
        return 80
    elif productInput == str(4):
        return 55
def selectProduct():
    itemInput = int(input("HOW MANY DO YOU NEED? : "))
    amount = producePrice(productInput)*itemInput
    return amount
def vatCal(price):
    amount = price*1.07
    return amount

login()
showMenu()
productInput = input("SELECT PRODUCE NUMBER : ")
while productInput != str(2) and productInput != str(1) and productInput != str(3) and productInput != str(4) :
    print("ERROR!! PLEASE SELECT NO. 1 TO 4")
    print("---------- ----------- ----------")
    productInput = (input("SELECT PRODUCE NUMBER AGAIN : "))
print("PRICE INCLUDES TEX :", vatCal(selectProduct()),"THB")
print("========== ========== ===========")
