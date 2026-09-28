num=int(input("Enter a number: "))
original=num
reversed=0
while original !=0:
    digit=original%10
    reversed=reversed*10+digit
    original=original//10
    print("reversed num:",reversed)