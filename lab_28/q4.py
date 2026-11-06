"""(4) A cloning construct (49 bp) contains a BamHI site, a short coding sequence and an
EcoRI site:
plasmid_seq = Seq("GGATCCTTATGGCTAGCAAAGGAGAAGAACTTTTCACTTAAGAATTCCC")
1. Create a SeqRecord with id and name PLAB001, set annotations[”molecule type”] =
”DNA”, and add three features: a misc feature for the BamHI site at 0-6, a CDS at 8-41
with qualifiers gene = labA and translation = MASKGEELFT, and a misc feature for
the EcoRI site at 41-47 (Python-style positions).
2. Write it to lab construct.gb in GenBank format; open the file in a text editor and
find the FEATURES table.
3. Read it back with SeqIO.read() and list every feature with its type, its 1-based start
and end, and its gene or note.
4. Extract the CDS, translate it, and check that the result matches the stored translation
qualifier."""
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature, SimpleLocation
from Bio.SeqRecord import SeqRecord

plasmid_seq = Seq("GGATCCTTATGGCTAGCAAAGGAGAAGAACTTTTCACTTAAGAATTCCC")

record = SeqRecord(
    plasmid_seq,
    id="PLAB001",
    name="PLAB001",
    description="Cloning construct with BamHI, CDS, and EcoRI",
)
record.annotations["molecule_type"] = "DNA"

bamhi_feat = SeqFeature(
    SimpleLocation(0, 6, strand=1), type="misc_feature", qualifiers={"note": ["BamHI site"]}
)
cds_feat = SeqFeature(
    SimpleLocation(8, 41, strand=1),
    type="CDS",
    qualifiers={"gene": ["labA"], "translation": ["MASKGEELFT"]},
)
ecori_feat = SeqFeature(
    SimpleLocation(41, 47, strand=1), type="misc_feature", qualifiers={"note": ["EcoRI site"]}
)

record.features.extend([bamhi_feat, cds_feat, ecori_feat])

SeqIO.write(record, "lab_construct.gb", "genbank")

gb_record = SeqIO.read("lab_construct.gb", "genbank")

print("Features in lab_construct.gb:")
for feature in gb_record.features:
  start_1based = int(feature.location.start) + 1
  end_1based = int(feature.location.end)

  if "gene" in feature.qualifiers:
    info = f"gene={feature.qualifiers['gene'][0]}"
  elif "note" in feature.qualifiers:
    info = f"note={feature.qualifiers['note'][0]}"
  else:
    info = "No gene/note"

  print(
      f"Type: {feature.type:<12} Location: {start_1based}-{end_1based:<6} Info:"
      f" {info}"
  )

print()

for feature in gb_record.features:
  if feature.type == "CDS":
    extracted_dna = feature.extract(gb_record.seq)
    translated_prot = str(extracted_dna.translate())
    stored_prot = feature.qualifiers["translation"][0]

    print(f"Extracted CDS Sequence: {extracted_dna}")
    print(f"Translated Protein:    {translated_prot}")
    print(f"Stored Translation:    {stored_prot}")
    print(f"Matches Stored:        {translated_prot == stored_prot}")