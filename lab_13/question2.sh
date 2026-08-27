cat > students.txt << 'EOF'
Ram 20 Biology
Sita 23 Maths
Gita 26 Physics
Suresh 23 Chemistry
EOF

echo "(i)The Age of person kesser than 25" 
awk '$2 <25 {print $1}' students.txt

echo "(ii)Physics score give"
awk '$3 == "Physics" {print $1}' students.txt

echo "(iii)Rewritng"
awk 'BEGIN{OFS = ","} {print $1,$2,$3}' students.txt > data2.csv

cat data2.csv
