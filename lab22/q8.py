def analyse_dna(sequence):
    sequence = sequence.upper()

    def gc_content():
        gc = sequence.count("G") + sequence.count("C")
        return (gc / len(sequence)) * 100

    gc_percent = gc_content()
    print(f"GC content: {gc_percent:.2f}%")

    if gc_percent > 50:
        print("The DNA is GC rich.")
    else:
        print("The DNA is AT rich.")

analyse_dna("ATGCGCGTAC")
