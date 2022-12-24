new=int(input("enter the number to squared : "))
a=0
b=0
d=0
e=0
while new>=1:
    a=new%10
    b=b*10+a
    d=a
    d=int(d)
    d=d*d
    e=e+d
    new=new/10
    new=int(new)
print(f"the square of each digit is {e} ")