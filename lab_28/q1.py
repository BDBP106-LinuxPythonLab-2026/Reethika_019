"""(1) The thrL gene of E. coli encodes a short leader peptide:
thrL = Seq("ATGAAACGCATTAGCACCACCATTACCACCACCATCACCATTACCACAGGTAACGGTGCGGGCTGA")
Print its length, its GC content as a percentage (2 decimal places), its translation with
and without to stop=True, the number of times ACC occurs, its last codon, and the first
12 bases of its reverse complement."""
from operator import countOf

import Bio
from Bio.Seq import Seq
thrL = Seq("ATGAAACGCATTAGCACCACCATTACCACCACCATCACCATTACCACAGGTAACGGTGCGGGCTGA")
print(len(thrL))
g_count=thrL.count('G')
c_count=thrL.count('C')
a_count=thrL.count('A')
t_count=thrL.count('T')
print("G count:",g_count,
      "C count:",c_count,
      "A_count:",a_count,
      "T count:",t_count,
)
gc_percentage = (g_count +c_count)/len(thrL)*100
print("GC_percentage:",round(gc_percentage,2))
print(thrL.translate())
print(thrL.translate(to_stop=True))
print(thrL.count('ACC'))
print(thrL.reverse_complement())
first_12= thrL.reverse_complement()[:12]
print(first_12)
last_codon = thrL[-3:]
print("Last codon:", last_codon)