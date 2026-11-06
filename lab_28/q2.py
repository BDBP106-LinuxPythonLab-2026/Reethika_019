"""(2) Do the following.
1. Read lab genes.fasta with SeqIO.parse() into a list and print how many records it has.
2. Print a table of ID, length, GC % (1 decimal place) and the protein translated up to
the first stop codon.
3. Write the genes with GC content of at least 50% to lab high gc.fasta, and print how
many were written.
4. Print the IDs sorted from highest to lowest GC content, using sorted() with a lambda."""
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

records = list(SeqIO.parse("lab_genes.fasta", "fasta"))
print("Total records:", len(records))
print()

print("ID\tLength\tGC%\tProtein")
for r in records:
  gc = round(gc_fraction(r.seq) * 100, 1)
  protein = r.seq.translate(to_stop=True)
  print(f"{r.id}\t{len(r.seq)}\t{gc}%\t{protein}")

print()

high_gc = [r for r in records if gc_fraction(r.seq) >= 0.5]
count = SeqIO.write(high_gc, "lab_high_gc.fasta", "fasta")
print("Written to file:", count)
print()

sorted_records = sorted(
    records, key=lambda r: gc_fraction(r.seq), reverse=True
)
print("Sorted by GC %:")
for r in sorted_records:
  print(f"{r.id}: {round(gc_fraction(r.seq)*100, 1)}%")
