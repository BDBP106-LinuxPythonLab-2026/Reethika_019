"""1. Number Classifier
Concepts: if/elif/else
Ask the user for an integer. Print whether it is positive, negative or zero. If it is non-zero,
also print whether it is even or odd. If it is divisible by both 3 and 5, print "FizzBuzz
number!".
Enter a number: -15
Negative, odd
FizzBuzz number!"""

n=int(input("Enter the value: "))
if n<0:
    print("The value is negative")
elif n>0:
    print("The value given is positive")
else:
    print("THe give number is 0")

if n%2==0:
    print("The given number is even")
else:
    print("The given number is odd")

if n%3==0 & n%5==0:
    print("FIZZBUZZ number!")
else:
    print("NOt a FIZZBUZZ number!")