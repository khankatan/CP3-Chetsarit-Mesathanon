life = 4
print("Question : How many years was the Buddha born before Jesus?")
anwInput = int(input("Answer : "))
while anwInput != 623:
    print(">>>>>>>>>>>>>>>>>>>> Wrong answer <<<<<<<<<<<<<<<<<<<<<<")
    life -= 1
    if life <= 0:
        print("======================= ========= ======================")
        print("----------------------- GAME OVER ----------------------")
        print("======================= ========= ======================")
        break
    print("Can answer more", life, "time")
    anwInput = int(input("Answer : "))
else:
    print(">>>>>>>>>>>>>>>>>>>> Correct answer <<<<<<<<<<<<<<<<<<<<")

if life > 0:
    print("Question : Decades, How many years?ี")
    anwInput = int(input("Answer : "))
    while anwInput != 10:
        print(">>>>>>>>>>>>>>>>>>>> Wrong answer <<<<<<<<<<<<<<<<<<<<<<")
        life -= 1
        if life <= 0:
            print("======================= ========= ======================")
            print("----------------------- GAME OVER ----------------------")
            print("======================= ========= ======================")
            break
        print("Can answer more", life, "time")
        anwInput = int(input("Answer : "))
    else:
        print(">>>>>>>>>>>>>>>>>>>> Correct answer <<<<<<<<<<<<<<<<<<<<")

if life > 0:
    print("Question : What is my name?")
    print("1) CHETSARIT MESATHANON")
    print("2) DAKOTA FANNING")
    print("3) MACKENZIE FOY")
    anwInput = int(input("Answer : "))
    while anwInput != 1:
        print(">>>>>>>>>>>>>>>>>>>> Wrong answer <<<<<<<<<<<<<<<<<<<<<<")
        life -= 1
        if life <= 0:
            print("======================= ========= ======================")
            print("----------------------- GAME OVER ----------------------")
            print("======================= ========= ======================")
            break
        print("Can answer more", life, "time")
        anwInput = int(input("Answer : "))
    else:
        print(">>>>>>>>>>>>>>>>>>>> Correct answer <<<<<<<<<<<<<<<<<<<<")