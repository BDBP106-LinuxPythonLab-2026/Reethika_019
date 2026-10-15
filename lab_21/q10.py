
"""(10) Extract vowels using list comprehension"""
text = input("Enter a string: ")
vowels = [ch for ch in text if ch.lower() in "aeiou"]
print(vowels)