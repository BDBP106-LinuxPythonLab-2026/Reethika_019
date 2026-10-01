# (2) Power (base ** n) using a loop
def power(base, n):
    result = 1
    for _ in range(n):
        result *= base
    return result
base = input("Enter BAASE number: ")
n=int(input("Enter n"))
print("2",power(base, n))
