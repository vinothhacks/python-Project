def cipher(text,shift,direct):
        cipher=""
        if(direct=="decode"):
            shift*=-1
        for letter in text:
            if letter in alpha:
                posit=alpha.index(letter)
                new_position=posit+shift
                new_letter=alpha[new_position]
                cipher+=new_letter
            else:
                cipher+=letter
        print(f"your {direct} code is {cipher}")

alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a=True
while(a):
    direct=input("enter decode or encode your message : ")
    text=input("type your message : ").lower()
    shift=int(input("enter the shift number : "))
    shift%=26    #it is to have bigger values for shit 
    cipher(text,shift,direct)
    b=input("do you want to decode and encode again say yes or no : ")
    if(b=="yes"):
        a=True
    else:
        a=False
        print("good bye have a great day !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")