def triangle_type(a, b, c):
    if a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    return "scalene"


print("Triangle Type")
print("3, 3, 3 is:", triangle_type(3, 3, 3))
print("5, 5, 8 is:", triangle_type(5, 5, 8))
print("3, 4, 5 is:", triangle_type(3, 4, 5))