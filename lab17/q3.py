# (3) Prime check
def is_prime(N):
    if N < 2:
        return False
        i = 2
        while i * i <= N:
            if N % i == 0:
                return False
            i += 1
        return True
N = int(input("Enter N: "))
print("prime" if is_prime(N) else "not prime")