from Bio import SeqIO
for seq_record in SeqIO.parse("ecoli_16s.fasta", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))