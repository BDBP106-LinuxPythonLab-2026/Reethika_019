x=int(input("Enter your x axis: "))
y=int(input("Enter your y axis: "))
if x>0 and y>0:
    print("X,Y lies in first quadrant")
elif x<0 and y>0:
    print("X,Y lies in second quadrant")
elif x>0 and y<0:
    print("X,Y lies in forth quadrant")
else:
    print("X,Y lies in 3rd quadrant")