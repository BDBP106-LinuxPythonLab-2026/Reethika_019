def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Running DNA analysis....")
        result = func(*args, **kwargs)
        print("Analysis complete!")
        return result
    return wrapper

@log_function_call
def gc_percentage(sequence):
    sequence = sequence.upper()
    gc = sequence.count("G") + sequence.count("C")
    return (gc / len(sequence)) * 100

print(f"GC%: {gc_percentage('ATGCGCGTAC'):.2f}")