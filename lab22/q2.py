"""(2) Fill in the correct piece of code below to create this decorator called before_after that
prints "Function is starting...." before the function call and prints "Function has finished!"
after the execution.
def before_after(func):
def wrapper():
<INSERT YOUR CODE HERE>
return wrapper
@before_after
def calculate():
print("Calculating...")
calculate()"""
def before_after(func):
    def wrapper():
        print("Function is starting....")
        func()
        print("Function has finished!")
    return wrapper
@before_after
def calculate():
    print("Calculating...")
calculate()