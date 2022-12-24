size=input("what size piza do you want S,M,L : ")
peppo=input("do you want to add pepporony Y or N : ")
cheese=input("do you want extra cheese Y or N : ")
bill=0
if(size=="l"):
    bill=25
elif(size=="m"):
    bill=20
else:
    bill=15
if(peppo=="y"):
    if(size=="m" or size=="l"):
        bill+=3
    if(size=="s"):
        bill+=2
else:
    print("no pepporoni added ")
if(cheese=="y"):
    bill+=1
    print("extra cheese added ")
else:
    print("no extra cheese added")
print("your bill ammount is ",bill)