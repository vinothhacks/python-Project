heig=input("enter the list of students to find their average : ").split()
print(heig)
for i in range(0,len(heig)):
    heig[i]=int(heig[i])
print(heig)
temp=0
#resulu=sum(heig)/len   it will also give the same answer
for height in heig:
    temp+=height
len=len(heig)
ave=temp/len
print("the average of their height is : ",ave)

