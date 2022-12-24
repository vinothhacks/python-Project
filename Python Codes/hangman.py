import random
words=["aeroplane","icecream","biriyani","chicken65","college","lucky","friends"]
word=random.choice(words)
length=len(word)
dump=[]
for i in range(0,length):
    dump+="$"
print(dump)
print(word)
ij=0
while (word!=dump):
    temp=input("enter a letter to find weather it is in the word : ")
    dump=[]
    for i in range(0,length):
            letter=word[i]
            if(letter==temp):
                    dump[i]=letter
                    print(dump)
            else:
                if(ij<6):
                    ij+=1
                else:
                    print("game over")