year=int(input("enter an year to find weather it is leap or not : "))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("it is a leap year")
        else:
            print("it is not a leap year")
    else:
        print("it is a leap year ")
else:
    print("not a leap year ")