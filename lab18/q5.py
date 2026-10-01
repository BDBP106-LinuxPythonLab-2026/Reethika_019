def remove_duplicate_words(sentence):
    seen = {}
    for w in sentence.split():
        seen[w] = True
    return " ".join(seen)

text = "the cat and the dog and the bird"
print("Remove Duplicate Words")
print("Original:", text)
print("Without duplicates:", remove_duplicate_words(text))