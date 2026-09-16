awk '$1 == "ATOM" && $4 == "PHE"' 1HK0.pdb > PHE_atoms.xyz
echo "PHE atoms saved to PHE_atoms.xyz"
wc -l PHE_atoms.xyz
