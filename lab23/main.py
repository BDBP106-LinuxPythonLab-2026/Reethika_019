from utils import math_utils,string_utils
num1=int(input("Enter your num1: "))
num2=int(input("Enter your num2: "))
print(math_utils.remainder(num1,num2))
print(math_utils.add(num1,num2))

str1,str2=map(str,input("Enter your string: ").split(","))
print(string_utils.upper_string(str1))