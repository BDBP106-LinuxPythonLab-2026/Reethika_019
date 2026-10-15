"""3. Guess the Number
Concepts: "until" loop (while True + break), if, counters
Store a secret number between 1 and 50. Keep asking the user to guess until they get it
right. After each wrong guess, print "Too high" or "Too low". When they get it, print how
many attempts it took. As a bonus, stop after 7 attempts and reveal the number."""
secret_number=14
count=0
while count<7:
    num=int(input("Enter the number: "))
    if num==secret_number:
        count=0
        print("correct the number is ",secret_number)
        break
    elif num != secret_number:
        count=count+1
        print("wrong and the number of attempts are",count)
    if count==7:
        print("limit reached")
        break
