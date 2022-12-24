a=int(input("enter upto what number do you wand to print hill : "))
list=[]
list1=[]
for i in range(1,a+1):
    list.append(i)
for i in range(1,a+1):
    list1.append(" ")
temp=a
temp1=-1
for i in range(1,a):
    temp=a-1
    temp1+=1
    print(list1[0:temp],list[0:temp1])
