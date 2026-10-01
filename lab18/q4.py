def most_unique_key(d):
    return max(d, key=lambda k: len(set(d[k])))

test_dict = {
    "Gfg": [5, 7, 7, 7, 7],
    "is": [6, 7, 7, 7],
    "Best": [9, 9, 6, 5, 5]
}
print("Task 4: Key with Most Unique Values")
print("Key with most unique values:", most_unique_key(test_dict))