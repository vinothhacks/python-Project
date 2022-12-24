import math
def calc(height,width,cover):
    temp=0
    temp=(height*width)/cover   #height * width is area /cover is for number of cans
    #temp=round(temp)
    temp=math.ceil(temp)
    return temp
heig=int(input("enter the height of the wall to be covered : "))
weid=int(input("enter the width of the wall to be covered : "))
cover=5     #because 1 paint can paints s square feets
temp=calc(heig,weid,cover)
print(f"the painting cans needed are : {temp}")