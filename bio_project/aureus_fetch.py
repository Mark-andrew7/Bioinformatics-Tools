from Bio import Entrez, SeqIO

Entrez.email = "markkamau56@gmail.com"

ecoli_id = "J01859.1"
handle = Entrez.efetch(db="nucleotide", id=ecoli_id, rettype="fasta", retmode="text")
ecoli_record = SeqIO.read(handle, "fasta")
handle.close()

sauereus_id = "NR_075000.1"
handle = Entrez.efetch()
saureus_record = SeqIO.read(handle, "fasta")
handle.close()

print(f"E.coli ID: {ecoli_record.id}")
print(f"S.aureus ID: {saureus_record.id}")
