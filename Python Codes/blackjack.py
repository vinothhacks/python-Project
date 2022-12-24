import random
j=10
q=10
k=10
a=[1,2,3,4,5,6,7,8,9,10,j,q,k,1,2,3,4,5,6,7,8,9,10,j,q,k,1,2,3,4,5,6,7,8,9,10,j,q,k,1,2,3,4,5,6,7,8,9,10,j,q,k,]
b=[]
c=[]
for i in range(1,3):
    b.append(random.choice(a))
    c.append(random.choice(a))
print(b)
print(c)

def new():
    b.append(random.choice(a))
    print(b)
def new1():
    c.append(random.choice(a))
    print(c)
temp=True
while(temp):
    su=0
    su1=0
    for i in b:
        su+=i
    for i in c:
        su1+=i
    if 11 in b and sum(b)>21:
        b.remove(11)
        b.append(1)
    if 11 in c and sum(c)>21:
        b.remove(11)
        b.append(1)
    if(su>=21):
        print("you lose")
        break
    elif(su1>=21):
        print("you win")
        break
    elif (11 in b) and (10 in b) and len(b)==2:
            print("you win")
            break
    elif (11 in c) and (10 in c) and len(c)==2:
            print("you loss")
            break
    temp1=True
    while(temp1):
        hi=input("do you want to hit or stand")
        if(hi=="hit"):
            new()
            temp1=False
        elif(hi=="stand"):
            if(su>su1):
                print("user wins")
                temp1=False
                temp=False
            elif(su==su1):
                print("match draw")
                temp1=False
                temp=False
            else:
                print("you lose")
                temp1=False
                temp=False
        if(sum(c)<17):
            new1()
            temp1=False

