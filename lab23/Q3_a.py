fout=open('stringmatrix.dat','w')
current_ascii=65
for row in range(3):
    row_char=[]
    for col in range(4):
        row_char.append(chr(current_ascii))
        current_ascii+=1
    fout.write(" ".join(row_char)+ "\n")
fout.close()






# Q3 b


grid = []
with open("stringmatrix.dat", "r") as file:
    for line in file:
        if line.strip():
            grid.append(line.split())

print("grid:")
print(grid)


columns = [list(col) for col in zip(*grid)]
print("\nColumns:")
print(columns)


rows = len(grid)
cols = len(grid[0])
diagonals = []

for d in range(rows + cols - 1):
    diag = []
    for r in range(rows):
        c = d - r
        if 0 <= c < cols:
            diag.append(grid[r][c])
    diagonals.append(diag)

print("\nDiagonals:")
print(diagonals)