from Bio import Entrez
from Bio import SeqIO

Entrez.email = "kamaumark19@gmail.com"

accession = "PP811674.1"
handle = Entrez.efetch(db="nucleotide", id=accession, rettype="fasta", retmode="text")
record = SeqIO.read(handle, "fasta")
handle.close()

print("ID:", record.id)
print("Description", record.description)
print("Length:", len(record.seq), "bp")
print("First 100 bases:", record.seq[:100])