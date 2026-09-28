word=input("Enter you word: ")
word=word.lower()
if word == word[::-1]:
    print("The given word is palindrome")
else:
    print("THe given word is not palindrome")