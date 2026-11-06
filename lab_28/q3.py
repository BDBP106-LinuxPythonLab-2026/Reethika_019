"""(3) A DNA fragment of unknown orientation:
mystery = Seq("CCATGGCTTGGAAATAGCATGCCCTAA")
1. Translate all six reading frames: frames +1, +2 and +3 start at positions 0, 1 and 2
of mystery; frames -1, -2 and -3 do the same on its reverse complement.
2. Find the longest open reading frame: a stretch that starts with M and ends at a stop
codon.
Hint: trim each frame to a multiple of 3 bases before translating (s[:len(s) - len(s) % 3]),
otherwise Biopython warns about a partial codon."""
from Bio.Seq import Seq

mystery = Seq("CCATGGCTTGGAAATAGCATGCCCTAA")

frames = {}

for i in range(3):
  sub_seq = mystery[i:]
  trimmed = sub_seq[: len(sub_seq) - len(sub_seq) % 3]
  frames[f"+{i+1}"] = trimmed.translate()
rev_comp = mystery.reverse_complement()
for i in range(3):
  sub_seq = rev_comp[i:]
  trimmed = sub_seq[: len(sub_seq) - len(sub_seq) % 3]
  frames[f"-{i+1}"] = trimmed.translate()

# 1. Print all six reading frames
print("Six Reading Frames:")
for name, prot in frames.items():
  print(f"Frame {name}: {prot}")

print()

longest_orf = ""
longest_frame = ""

for name, prot in frames.items():
  prot_str = str(prot)
  for start in range(len(prot_str)):
    if prot_str[start] == "M":
      stop = prot_str.find("*", start)
      if stop != -1:
        orf = prot_str[start : stop + 1]
        if len(orf) > len(longest_orf):
          longest_orf = orf
          longest_frame = name

print("Longest Open Reading Frame:")
print(f"Frame: {longest_frame}")
print(f"Protein: {longest_orf}")
print(f"Length: {len(longest_orf)} amino acids")