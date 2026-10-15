"""(11) Concatenate strings into a sentence using reduce"""
from functools import reduce

words = ["Python", "is", "easy", "to", "learn"]
sentence = reduce(lambda a, b: a + " " + b, words)
print(sentence)