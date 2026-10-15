"""(3) Write a decorator called count_calls that counts how many times a function is called
and prints the count. Use the template code below and fill in the correct piece of code.
def count_calls(func):
count = 0
def wrapper():
<INSERT YOUR CODE HERE>
return wrapper
@count_calls
def say_hi():
print("Hi!")
say_hi()
say_hi()
say_hi()
The expected output is
Hi!
Call count: 1
Hi!

Call count: 2
Hi!
Call count: 3"""
def count_calls(func):
    count = 0
    def wrapper():
        wrapper.count += 1
        func()
        print("Call count:", wrapper.count)
    wrapper.count = count
    return wrapper

@count_calls
def say_hi():
    print("Hi!")

say_hi()
say_hi()
say_hi()

