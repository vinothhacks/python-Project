import random
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("welocome to number guessing game")
print("i am thinking of number between number between 1 t0 100")
i=True
while(i):
    a=input("choose the difficulty type easy or hard : ")
    n=0
    if(a=="hard"):
        n=5
        i=False
    elif(a=="easy"):
        n=10
        i=False
    else:
        print("invalide word is been typed ")
b=random.randint(1,100)
while(n>0):
    print(f"you have {n} attempts more")
    c=int(input("make a guess : "))
    if(b==c):
        print("you won ")
        print(f"the random variable is {b} ")
        break
    elif(b>100):
        print("value is greater then 100")
    elif(b<0):
        print("value is less then 0")
    elif(c<b):
        print("too low")
        n=n-1
    elif(c>b):
        print("too high")
        print('guess again')
        n=n-1
    if(n==0):
        print("game over you lossss")
