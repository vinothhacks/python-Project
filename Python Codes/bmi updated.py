weight=int(input("enter the weight of your body : "))
height=float(input("enter the height of your body in meters : "))
print(weight ,"\n", height)
bmi=weight/(height*height)
print("your body bmi is ",bmi)
if (bmi<=18.5):
    print("underweight")
elif (bmi>18.5 and bmi<=25):
    print("normal weight")
elif (bmi>25 and bmi<=30):
    print("over weight")
elif (bmi>30 and bmi<35):
    print("obese")
else:
    print("today night at 11.55 you will be dead tommorow is your funural")