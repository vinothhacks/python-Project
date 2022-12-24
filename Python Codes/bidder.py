a=True
dic={}
while(a):
    a=input("what is your name : ")
    b=int(input("what is your bid : "))
    c=input("are there any other bidders : type yes or no ")
    dic[a]=b
    if(c=="yes"):
        print("\n \n \n \n \n")
    elif(c=="no"):
        a=False
temp=0
for i in dic:
    if(dic[i]>=temp):
        temp=dic[i]
        max=i
print("the winner is ",max)
    