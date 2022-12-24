n=int(input("enter how many number to be displayed : "))
x=int(input("enter the starting number : "))
y=int(input("enter the numbers to be divisible after starting point : "))
list=[]
while(n>0):
    if x%y==0:
        list.append(x)
        n-=1
    x+=1
for i in list:
    print(i)