from tkinter.tix import INTEGER


print("only two digit numbers")
n=int(input("enter the two digit number :"))
print(type(n))
a=n%10
print(a)
b=n/10
print(b)
b=int(b)        #in here the b will be converted into integer
print(b)        
print(a+b)