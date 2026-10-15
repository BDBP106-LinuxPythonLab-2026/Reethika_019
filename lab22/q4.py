"""(4) Write a decorator called check_positive that checks whether the argument passed to
a function is positive. If it is positive, execute the function; otherwise, print
"Number must be positive"."""


def check_positive(func):
    def wrapper(n,*args, **kwargs):
        if n > 0:
            print(func(func.__name__,*args, **kwargs))
        else:
            print("Number must be positive")
    return wrapper

@check_positive
def display_number(n):
    print("The number is ",n)
display_number(-15)
display_number(10)