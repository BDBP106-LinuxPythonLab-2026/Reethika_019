"""(5) Sum of a list using lambda and reduce"""
from functools import reduce

numbers = [10, 20, 30, 40]
total = reduce(lambda x, y: x + y, numbers)
print("Sum:", total)
