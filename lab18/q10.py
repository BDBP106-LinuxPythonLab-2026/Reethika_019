def next_prime(n):
    def is_prime(x):
        if x < 2:
            return False
        i = 2
        while i * i <= x:
            if x % i == 0:
                return False
            i += 1
        return True

    n += 1
    while not is_prime(n):
        n += 1
    return n

num = int(input("Enter an integer: "))
print("Next Prime Number")
print(f"First prime larger than {num} is:", next_prime(num))