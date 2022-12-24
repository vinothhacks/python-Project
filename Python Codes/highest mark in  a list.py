mark=input("enter the list of students mark to find the highest mark : ").split()
for i in range(0,len(mark)):
    mark[i]=int(mark[i])
print(mark)
#max(mark)  will also give the output
#min(mark)  will give the lowest value
temp=0
for i in mark:
    if(temp<i):
        temp=i
print(f"the highest mark in the list of students is : {temp}")
