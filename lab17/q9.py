# (9) Anagram check
def is_anagram(a, b):
    return sorted(a.lower()) ==sorted(b.lower())