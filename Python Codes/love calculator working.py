boy=input("enter the name of the boy : ")
girl=input("enter the name of the girl : ")
boy=boy.lower()
girl=girl.lower()
combine=boy+girl
t=combine.count("t")
r=combine.count("r")
u=combine.count("u")
e=combine.count("e")
true=t+r+u+e
l=combine.count("l")
o=combine.count("o")
v=combine.count("v")
e=combine.count("e")
love=l+o+v+e
score=str(true)+str(love)
print("your love score is : ",score)
score=int(score)
if(score<10 or score>90):
    print(f"your score is {score}, you go together like coke and mentos")
elif(score>40 and score<50):
    print(f"your score is {score}, you are alright together")
else:
    print(f"your score is {score}")
 