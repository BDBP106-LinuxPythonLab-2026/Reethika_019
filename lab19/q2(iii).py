s=[n for n in range(2,51) if all(n%d !=0 for d in range(2,int(n**0.5)+1))]
a=[i for i in range(51) if i%2==0]
print(s)
print(a)
common = list(set(a) & set(s))
print(common)


common = [item for item in s if item in a]
print(common)