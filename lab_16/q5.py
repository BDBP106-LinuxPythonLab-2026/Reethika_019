import math
b,a,c=map(float,input("Enter your values: ").split(",1"))
D=b**2-4*a*c
if D>0:
    r1=(-b+math.sqrt(D))/(2*a)
    r2=(-b-math.sqrt(D))/(2*a)
    print("r1:",r1)
    print("r2:",r2)
elif D==0:
    r=-b/2*a
    print("r:",r)
else:
    real=-b/(2*a)
    print("real:",real)
    imag=math.sqrt(-D)/(2*a)
    print("imag:",imag)
    print("Complex roots:",real,"+",imag,"i and",real,"-",imag,"i")