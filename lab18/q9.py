def codons(seq, pos):
    return [seq[i:i + 3] for i in range(pos - 1, len(seq) - 2, 3)]

# Test run
dna_sequence = "GTTTCGATTATAACG"
print("Extract Codons")
print("Sequence:", dna_sequence)
print("Reading from position 1:", codons(dna_sequence, 1))
print("Reading from position 3:", codons(dna_sequence, 3))