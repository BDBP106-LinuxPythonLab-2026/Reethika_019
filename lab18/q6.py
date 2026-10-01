def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

a, b, c = 3, 4, 5
print("Triangle Area")
print(f"Area of triangle ({a}, {b}, {c}):", triangle_area(a, b, c))