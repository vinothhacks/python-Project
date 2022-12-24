print("welcome to tip calculator")
ammount=float(input("what is the total bill ammount : $"))
tip=float(input("what percentage do you want to tip :"))
tip=ammount*tip/100
ammount+=tip
share=float(input("how many people to split he bill ? "))
share=ammount/share
print("each persn should pay : $",share)