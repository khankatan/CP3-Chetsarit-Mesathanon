print("========== L O N G I N ==========")
user1 = input("Username : ")
pass1 = input("Password : ")
print("---------- ----------- ----------")
if user1 == "chetsarit" and pass1 == "71037":
    print("WELCOME TO GUPPEE DRINKS")
    print("---------- ----------- ----------")
    print("PLEASE SELECT A PRODUCT")
    print("1) COCONUT JUICE     : 100 THB")
    print("2) ORANGE JUICE      : 60  THB")
    print("3) LAMONEDE JUICE    : 80  THB")
    print("4) WATER MALON JUICE : 55  THB")
    print("---------- ----------- ----------")
    productInput = int(input("SELECT PRODUCE NUMBER : "))
    while range(1,4):
        if productInput == 1:
            itemInput = int(input("HOW MANY DO YOU NEED? : "))
            print("TOTAL AMOUNT :", 100*itemInput, "THB")
            break
        elif productInput == 2:
            itemInput = int(input("HOW MANY DO YOU NEED? : "))
            print("TOTAL AMOUNT :", 60*itemInput, "THB")
            break
        elif productInput == 3:
            itemInput = int(input("HOW MANY DO YOU NEED? : "))
            print("TOTAL AMOUNT :", 80*itemInput, "THB")
            break
        elif productInput == 4:
            itemInput = int(input("HOW MANY DO YOU NEED? : "))
            print("TOTAL AMOUNT :", 55*itemInput, "THB")
            break
        else:
            print("---------- ----------- ----------")
            print("ERROR!! PLEASE SELECT NO. 1 TO 4")
            print("---------- ----------- ----------")
            productInput = int(input("SELECT PRODUCE NUMBER AGAIN : "))
else:
    print("ERROR!!")
print("========== ========== ===========")