import random
print("welcome to pypassword generator : ")
letter=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
number=["1","2","3","4","5","6","7","8","9","0"]
symbol=["!","@","#","$","%","^","&","*","(",")","_","+","~"]
let=int(input("how many letters would you like in the password ? "))
sym=int(input("how many symbols would you like in the password ? "))
num=int(input("how many numbers would you like to have in the passsword ? "))
len_pass=let+sym+num
temp=0
temp1=0
temp2=0
password=""
password1=""
password2=""
for i in range(0,let):
        temp=random.choice(letter)
        password+=temp
        print(password)
for i in range(0,sym):
        temp1=random.choice(symbol)
        password1+=temp1
        print(password1)
for i in range(0,num):
        temp2=random.choice(number)
        password2+=temp2
        print(password2)
print(f"the password is : {password}{password1}{password2}")
