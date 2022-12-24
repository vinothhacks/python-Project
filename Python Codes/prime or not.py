def prime(n):
    prime=True
    for i in range(2,n):
        if(n%i==0):
            prime=False
    if(prime):
        print("it is a prime number ")
    else:
        print("it is not a prime number ")
n=int(input("enter the input number to check weather the number is prime or not : "))
prime(n)
