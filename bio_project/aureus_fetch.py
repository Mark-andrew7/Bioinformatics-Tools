from Bio import Entrez, SeqIO
from Bio import pairwise2

Entrez.email = "markkamau56@gmail.com"

ecoli_id = "J01859.1"
handle = Entrez.efetch(db="nucleotide", id=ecoli_id, rettype="fasta", retmode="text")
ecoli_record = SeqIO.read(handle, "fasta")
handle.close()

sauereus_id = "NR_075000.1"
handle = Entrez.efetch(db="nucleotide", id = sauereus_id, rettype="fasta", retmode="text")
saureus_record = SeqIO.read(handle, "fasta")
handle.close()

print(f"E.coli ID: {ecoli_record.id}")
print(f"S.aureus ID: {saureus_record.id}")

ecoli_seq = ecoli_record.seq
saureus_seq = saureus_record.seq

alignments = pairwise2.align.globalxx(ecoli_seq, saureus_seq)
top_alignment = alignments[0]
score = top_alignment.score
print(f"Alignment score: {score}")

print(pairwise2.format_alignment(*top_alignment))