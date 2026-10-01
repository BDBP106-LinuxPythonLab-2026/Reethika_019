#(4) Individual digits of N
def print_digits(N):
    for d in str(abs(N)):
        print(d)
N=input("Enter N:")
print_digits(N)