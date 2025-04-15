from Bio import Entrez, SeqIO
from Bio.SeqUtils import gc_fraction

Entrez.email = "kamaumark19@gmail.com"

sequence_id = "J01859.1"
handle = Entrez.efetch(db="nucleotide", id=sequence_id, rettype="fasta", retmode="text")
record = SeqIO.read(handle, "fasta")
handle.close()

sequence = record.seq
length = len(sequence)
gc_content = gc_fraction(sequence) * 100

print(f"Sequence ID: {record.id}")
print(f"Description: {record.description}")
print(f"Sequence: {sequence}")
print(f"Length: {length}")
print(f"GC content: {gc_content:.2f}")