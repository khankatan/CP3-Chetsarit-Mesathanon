def plusNum(x,y):
    print("ผลลัพธ์การบวก =",x+y)
def minusNum(x,y):
    print("ผลลัพธ์การลบ =",x-y)
def multiNum(x,y):
    print("ผลลัพธ์การคูณ =",x*y)
def divideNum(x,y):
    print("ผลลัพธ์การหาร =",x/y)

x = int(input("เลขตั้งต้น : "))
y = int(input("เลขกระทำ : "))

plusNum(x,y)
minusNum(x,y)
multiNum(x,y)
divideNum(x,y)