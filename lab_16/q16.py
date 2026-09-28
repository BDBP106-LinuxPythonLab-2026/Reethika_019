a,b,c=map(int,input("Enter the values of a,b,c: ").split(","))
if a+b>c and b+c>a and c+a>b:
    if a == b == c:
        print("Equilateral Triangle")
    elif a==b or b==c or a==c:
        print("Isosceles Triangle")
    else:
        print("scalenos Triangle")
else:
    print("Not a trangle")