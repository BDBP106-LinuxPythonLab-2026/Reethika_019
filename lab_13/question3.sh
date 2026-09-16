cat > sequence.fasta << 'EOF'
>seq1
ATGCTAGCTAGAGGTCTAGG
>seq2
TTAGGCATGCATTAAGTCATTA
EOF

echo "(i) REmove line containing >(header lines)"
awk '!/^>/' sequence.fasta

echo "(ii) DNA into RNA sequence"
sed '/^>/!s/T/U/g' sequence.fasta

echo "(iii)Replace seq1"
sed 's/seq1/human_gene/' sequence.fasta
