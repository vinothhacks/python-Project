score={
    "harry":81,
    "ron":78,
    "hermoine":99,
    "draco":74,
    "neville":62,
} 
temp=0
grade={}
for i in score:
    temp=score[i]
    if(temp>90 and temp<=100):
        grade[i]="outstanding "
    elif(temp>80 and temp<=90):
        grade[i]="exceeds expectation"
    elif(temp>70 and temp<=80):
        grade[i]="acceptable"
    elif(temp<=70):
        grade[i]="fail"

print(grade)

for i in grade:
    print(i," grade is : ",grade[i])