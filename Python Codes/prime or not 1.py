for i in range(1,100):
    count=0
    for j in range(2,i//2+1):
        if(i%j==0):
            count+=1
            break
    if(count==0 and i!=1):
        print(f"{i} is a prime number ")