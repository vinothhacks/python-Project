pan=int(input("enter the number to be reversed : "))
temp=0
a=0
palindrome=pan
while(pan>1):
    temp=pan%10
    a=a*10+temp
    a=int(a)
    pan=pan/10
print(a)
if(palindrome==a):
    print("the number is a palindrome $$")
else:
    print("the number is not a palindrome $$")