num=int(input("Enter a number:"))
total=0
while num!=0:
    x=num%10
    total=total+x
    num=num//10
print("Total:",total)