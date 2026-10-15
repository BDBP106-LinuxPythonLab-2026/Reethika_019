"""Write a decorator measure_time to calculate how long a function takes to run. Use it
on a function that calculates the factorial of a number. Use a test case of calculating the
factorial of 50."""
import time
import math
def measure_time(func):
    def wrapper(*args,**kwargs):
        begin=time.time()
        func(*args,**kwargs)
        end=time.time()
        print("The time taken is ",func.__name__,end-begin)
    return wrapper
@measure_time
def fact(n):
    print(math.factorial(n))
fact(50)