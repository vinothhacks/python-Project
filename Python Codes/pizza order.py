size=input("what size piza do you want S,M,L : ")
peppo=input("what pepporoni do you want S OR L : ")
cheese=input("do you want extra cheese Y or N : ")
bill=0
if(size=="s"):
    print("small pizza")
    bill=15
    if(peppo=="s"):
        print("pepporonies added for extra 2 dollers")
        bill+=2
    if(cheese=="y"):
        print("extra cheese for 1 doller")
        bill+=1
    print(f"total bill of your pizza is {bill}")
elif(size=="m"):
   print("medium pizza")
   bill=20
   if(peppo=="y"):
        print("pepporoni added for 3 doller")
        bill+=3
    if(cheese=="y"):
        print("extra cheese for 1 doller")
        bill+=1
    print(f"total bill of your pizza is {bill}")
elif(size=="l"):
    print("large pizza")
    bill=25
    if(peppo=="y"):
        print("pepporoni added for 3 doller")
        bill+=3
    if(cheese=="y"):
        print("extra cheese for 1 doller")
        bill+=1
    print(f"total bill of your pizza is {bill}")
    