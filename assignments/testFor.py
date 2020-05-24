roundInput = int(input("enter round number : "))
sum = 0
for x in range(roundInput):
    numberInput = input("X"+str(x+1)+" = ")
    sum += int(numberInput)
print("total plus =",sum)