print("to print each number from 1 to 100 in there divisible  3 is 'fizz' 5 is 'buzz' 3and 5 is 'fizz buzz'")
for i in range(1,101,1):
    if(i%3!=0 and i%5!=0):
        print(i)
    elif(i%3==0 and i%5==0):
        print("fizz buzz")
    elif(i%3==0):
        print("fizz")
    elif(i%5==0):
        print("buzz")
   #else:           otherwise this will print all other digits
   #    print(i)
