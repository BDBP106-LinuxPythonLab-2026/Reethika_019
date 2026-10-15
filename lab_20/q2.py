"""2. Vowel and Consonant Counter
Concepts: for loop over a string, lower(), isalpha(), membership with in
Read a sentence. Count the vowels, consonants, digits and spaces. Ignore case and
punctuation.
Enter text: Hello World 2026!
Vowels: 3 Consonants: 7 Digits: 4 Spaces: 2"""

line="Hello World 2026!"
vowels="aeiou"
vowel_count=0
consonant_count=0
digit_count=0
space_count=0
for char in line:
    if char in vowels:
        vowel_count+=1
    elif char.isalpha():
        consonant_count=consonant_count+1
    elif char.isdigit():
        digit_count=digit_count+1
    elif char ==' ':
        space_count+=1
print(f'Vowel count:{vowel_count} ,Consonant count:{consonant_count} ,Digit count:{digit_count} ,Space count:{space_count}')


