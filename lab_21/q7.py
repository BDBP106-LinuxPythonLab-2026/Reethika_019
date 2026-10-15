"""Write a function analyse_dna(sequence) that defines an inner function gc_content()
to calculate GC% . The outer function should print whether the given DNA is AT rich
or GC rich sequence."""
def analyse_dna(sequence):
    sequence = sequence.upper()
    def gc_content():
        gc_count=sequence.count("G")+sequence.count("C")
        percentage_gc=(gc_count/len(sequence))*100
        return percentage_gc
    gc_percent=gc_content()
    if gc_percent>50:
        print("GC rich sequence")
    elif gc_percent<50:
        print("AT rich squence")

DNA_squence=("ATGCGATCGGC")
analyse_dna(DNA_squence)
