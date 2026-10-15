"""fill in the correct piece of code below to make this decorator called greet_decorator
work. Show that it works by taking a screenshot of the code and its output.
def greet_decorator(func):
def wrapper():
<INSERT YOUR CODE HERE>
return wrapper
@greet_decorator
def message():
print("This is my first attempt at using decorator.")"""
def greet_decorator(func):
    def wrapper():
        func()
    return wrapper
@greet_decorator
def message():
    print("This is my first attempt at using decorator.")
message()