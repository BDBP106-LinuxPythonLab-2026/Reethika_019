num=int(input("Enter your input"))
original = num
reversed=0
while num !=0:
    digit=num%10
    reversed=reversed*10+digit
    num=num//10
    print("reversed:",reversed)
if original == reversed:
    print("Palindrome sequence")
else:
    print("Not Palindrome")
