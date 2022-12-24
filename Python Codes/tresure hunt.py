row1=["*","*","*"]
row2=["*","*","*"]
row3=["*","*","*"]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}\n")
pos=input("where do you want to put the tresure colume and row : ")
print(type(pos))
row=int(pos[0])
colume=int(pos[1])
row_fin=map[row-1]     
row_fin[colume-1]="X"
#map[colume-1][row-1]="X"
print(f"{row1}\n{row2}\n{row3}\n")


