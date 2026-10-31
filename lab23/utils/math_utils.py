def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    if b==0:
        print("Error: Division by zero is not allowed")
    else:
        return a/b

def remainder(a,b):
    if b==0:
        print("Error: Division by zero is not allowed")
    else:
        return a%b