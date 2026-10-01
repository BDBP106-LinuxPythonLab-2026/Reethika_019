#a
a=[i for i in range(51) if i%2==0]
print(a)
for n in a:
    #print(n)
    c=",".join(str(i) for i in a)
    print("c=",c)
    print(type(c))
    break
#b
a=[i for i in range(51) if i%2==0]
print(a)
for n in a:
    #print(n)
    c=".".join(str(i) for i in a)
    print("c=",c)
    print(type(c))
    break
#c
a=[i for i in range(51) if i%2==0]
print(a)
for n in a:
    #print(n)
    c="_".join(str(i) for i in a)
    print("c=",c)
    print(type(c))
    break

#d
for n in range(51):
    c=n**2
    print(n,c)