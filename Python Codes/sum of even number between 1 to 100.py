print("to add all the even numbers from 1 t0 100 : ")
temp=0
for i in range(1,101,1):
    if(i%2==0):
        temp+=i
        print(i,"\t",temp)
print(f"the sum of numbers between 1 to 100 is : {temp}")
