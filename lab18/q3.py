def max_min(d):
    return max(d.values()), min(d.values())

sample_dict = {"a": 10, "b": 25, "c": 7}
print("Max and Min Values")
max_val, min_val = max_min(sample_dict)
print("Maximum value:", max_val)
print("Minimum value:", min_val)