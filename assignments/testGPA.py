score = int(input("YOUR SCORE : "))
if score > 100 or score < 0:
    print("ERROR!!!")
elif score >= 80:
    print("GRAD A")
elif score >= 75:
    print("GRAD B+")
elif score >= 70:
    print("GRAD B")
elif score >= 65:
    print("GRAD C+")
elif score >= 60:
    print("GRAD C")
elif score >= 55:
    print("GRAD D+")
elif score >= 50:
    print("GRAD D")
elif score < 50:
    print("GRAD F")