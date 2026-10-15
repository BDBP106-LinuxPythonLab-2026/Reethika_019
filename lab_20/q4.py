"""4. Multiplication Table Grid
Concepts: nested for loops, range(), string alignment with rjust()

Ask for a number n. Print an n × n multiplication table with neatly aligned columns and a
header row.
1 2 3 4
1 1 2 3 4
2 2 4 6 8
3 3 6 9 12
4 4 8 12 16"""

n=int(input("Enter your number"))
width=len(str(n*n))+1
print(" "*width,end=" ")
for j in range(1,n+1):
    print(str(j).rjust(width),end=" ")
print()
for i in range(1,n+1):
    print(str(i).rjust(width),end=" ")
    for j in range(1,n+1):
        print(str(i*j).rjust(width),end=" ")
    print()
