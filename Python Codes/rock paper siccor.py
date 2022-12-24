import random
use=int(input("what do you choose : 0=rock , 1=paper , 2=siccor "))
com=int(random.randint(0,2))
print(f"computer choice is {com} ")
if(com==use):
    print("draw")
elif(use==0 and com==2):
    print("user winnes")
elif(use==1 and com==0):
    print("user winnns")
elif(use==2 and com==1):
    print("user winnns")
else:
    if(use>=3 or use<0):
        print("invalid number")
    else:
        print("computer winns")