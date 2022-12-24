def encode(text,shift):
    cipher=""
    for letter in text:
        posit=alpha.index(letter)
        new_position=posit+shift
        new_letter=alpha[new_position]
        cipher+=new_letter
    print(f"your cipher code is {cipher}")

def decode(text,shift):
    cipher=""
    for letter in text:
        posit=alpha.index(letter)
        new_position=posit-shift
        new_letter=alpha[new_position]
        cipher+=new_letter
    print(f"the decoded cipher is : {cipher}")
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direct=input("enter decode or encode your message : ")
text=input("type your message : ").lower()
shift=int(input("enter the shift number : "))
again=True
while(again):
    if(direct=="encode"):
        encode(text,shift)
    elif(direct=="decode"):
        decode(text,shift)
    else:
        print("invalid statement ")
    a=input("do youe want to encode and decode again yes or no : ")
    if(a=="no"):
        again=False