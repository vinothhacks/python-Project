from operator import truediv


def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
dic={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}
temp=True
while(temp):
    a=int(input("enter the first number : "))
    c=int(input("enter the second number : "))
    for i in dic:
        print(i)
    b=input("enter the operator to perform the operation : ")
    """if (b=="+"):
        answer=add(a,c)
    elif (b=="-"):
        answer=sub(a,c)
    elif (b=="+"):
        answer=mul(a,c)
    elif (b=="+"):
        answer=div(a,c)
    """
    answer=dic[b]
    answer=answer(a,c)
    print(f"{a}{b}{c}={answer}")
    temp1=True
    while(temp1):    
        d=input(f"do you want continue with {answer} type y or for new caluculation type n or to finish end : ")
        if(d=="y"):
            oper=input("enter another operator to continue : ")
            e=int(input("enter the new number : "))
            answer=dic[oper]
            answer=answer(answer(a,c),e)
            print(answer)
        elif(d=="n"):
            temp1=0
        elif(d=="end"):
            temp1=0
            temp=0