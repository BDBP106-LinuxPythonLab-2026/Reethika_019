"""(4) Filter the odd elements of the first n Fibonacci terms"""
n = int(input("Enter n: "))

fib = []
a, b = 0, 1
for _ in range(n):
    fib.append(a)
    a, b = b, a + b

odd_elements = list(filter(lambda x: x % 2 != 0, fib))
print("Fibonacci:", fib)
print("Odd elements:", odd_elements)