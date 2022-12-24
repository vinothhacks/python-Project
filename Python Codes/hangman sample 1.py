import random
words=["mouse","aeroplane","icecream","biriyani","chicken65","college"]
word=random.choice(words)
length=len(word)
dump=[]
for i in range(length): #last number will not be considered
    dump+="-"
print(dump)
print(word)
end=False
life=6
live=0
print("total you have six lifes")
while(not end):
    temp=input("enter a letter to find weather it is in the word : ").lower()
    for i in range(length):
        letter=word[i]
        if(letter==temp):
            dump[i]=letter
    if temp not in word:
        live+=1
        print(live,"life over")
        life-=1
        if(life==0):
                print("game over")
                end=True
                print(f"the correct word is {word}")
        #else:
        #print("-")
    print(dump)
    if "-" not in dump:
            print("you win")
            end=True
