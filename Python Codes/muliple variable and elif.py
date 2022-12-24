#height,age=input("enter your height and the age").split()  error if you make it as int
height,age=[int(height) for height in input("enter the height and the age : ").split()]
if (height <=120):
    print("first grow then come to ride the roller ghoster ")
else:
    print("you can enter the roller ghoster sir ")
if (age<=16):
    print("your ticket price 2 dollere for kids")
elif (age<=30):
    print("your ticket cost is 4 doller for adult")
elif (age>30):
    print("for you age you are not even allowed go and get black ticket ")