print("========== L O N G I N ==========")
user1 = input("Username : ")
pass1 = input("Password : ")

while user1 != "admin" or pass1 != "1234":
    print("---------- ----------- ----------")
    print("Username or Password Incorrect!!")
    print("Please enter again")
    user1 = input("Username : ")
    pass1 = input("Password : ")

else :
    print("---------- ----------- ----------")
    print("    WELCOME TO GUPPEE DRINKS")
    print("---------- ----------- ----------")
    print("PLEASE SELECT A PRODUCT")
    print("1) COCONUT JUICE     : 100 THB")
    print("2) ORANGE JUICE      : 60  THB")
    print("3) LAMONEDE JUICE    : 80  THB")
    print("4) WATER MALON JUICE : 55  THB")
    print("---------- ----------- ----------")
    productInput = input("SELECT PRODUCE NUMBER : ")
    while productInput:
        if productInput == str(1):
            itemInput = int(input("HOW MANY DO YOU NEED? : "))
            print("TOTAL AMOUNT :", 100*itemInput, "THB")
            break
        elif productInput == str(2):
            itemInput = int(input("HOW MANY DO YOU NEED? : "))
            print("TOTAL AMOUNT :", 60*itemInput, "THB")
            break
        elif productInput == str(3):
            itemInput = int(input("HOW MANY DO YOU NEED? : "))
            print("TOTAL AMOUNT :", 80*itemInput, "THB")
            break
        elif productInput == str(4):
            itemInput = int(input("HOW MANY DO YOU NEED? : "))
            print("TOTAL AMOUNT :", 55*itemInput, "THB")
            break
        else:
            print("---------- ----------- ----------")
            print("ERROR!! PLEASE SELECT NO. 1 TO 4")
            print("---------- ----------- ----------")
            productInput = (input("SELECT PRODUCE NUMBER AGAIN : "))

print("========== ========== ===========")