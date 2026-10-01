s=[n for n in range(2,51) if all(n%d !=0 for d in range(2,int(n**0.5)+1))]
print(s)


