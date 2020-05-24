print("========== L O N G I N ==========")
user1 = input("Username : ")
pass1 = input("Password : ")
timeLog = 3
while user1 != "admin" or pass1 != "1234":
    timeLog -= 1
    print("---------- ----------- ----------")
    if timeLog == 0:
        print("Wait 15 minutes")
        break
    print("Username or Password Incorrect!!")
    print("Please enter again")
    user1 = input("Username : ")
    pass1 = input("Password : ")
else:
    print("---------- ----------- ----------")
    print("Done . . .")
print("========== =========== ===========")