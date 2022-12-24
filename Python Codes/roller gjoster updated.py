#height,age=input("enter your height and the age").split()  error if you make it as int
height,age=[int(height) for height in input("enter the height and the age : ").split()]
bill=0
if (height >=120):
    print("you can enter the roller ghoster sir ")
    if (age<=16):
        bill=2
        print("your ticket price 2 dollere for kids")
    elif (age<=30):
        bill=4
        print("your ticket cost is 4 doller for adult")
    elif (age>30):
        bill=10
        print("for you age you are not even allowed go and get black ticket ")
    pic=input("do you want to take photo or not say yes or no : ")
    if(pic=="yes"):
        bill+=2
        print("for photos 2 dollers your total bill is ",bill)
    if(pic=="no"):
        print("then your total bill will be ",bill) 
        
else:
    print("first grow then come to ride the roller ghoster ")