#lab_15(sep-03-2026)
#question 1
import math
print(math.floor(2.7/2))
print(math.ceil(2.7/2))
print(int(2.7/2))
a=(10+5j/2)
print("a=",a.real)
print("a=",a.imag)
complex(2.2,5.3).conjugate()
b=round(2.5)
print("b=",b)
e=round(-2.5)
print("e=",e)
f=3*2**2
print("f=",f)
d=3**2*2
print("d=",d)
m=7//4
print("m=",m)
g=7%4
print("g=",g)
#t=(-7%4)
t=((-8+1)%4)
print("t=",t)

#question2

a=1;b=2;c=4
r=(a and b)
print("r=",r)

q=(not a<b or c>b)
print("q=",q)

print(type(complex(a,b+c).real)is int)
print(type(complex(a,b+c).imag))

#question3

k=3;n=5
print("k+n=",k+n)
print("k-n=",k-n)
print("k++n=",k++n)
print("k**n=",k**n)
print("k%n=",k%n)
print("k//n=",k//n)
print("k/n=",k/n)
print("k>n=",bool(k>n))
print("k<n=",bool(k<n))
print("k*n=",k*n)


#question 4
import cmath
a=float(input("Enter the value of a: "))
b=float(input("Enter the value of b: "))
c=float(input("Enter the value of c: "))
d=(b**2)-(4*a*c)
r1=(-b+ cmath.sqrt(d))/(2*a)
r2=(-b- cmath.sqrt(d))/(2*a)
print("r1=",r1)
print("r2=",r2)