import pandas as pd
import numpy as np
from Bio import SeqIO
import string,csv

with open('GCF_AlkB_cleaned_1_out.csv','r') as f:
    GCF = [line.rstrip() for line in f]
df = pd.DataFrame()
df['Sequence'] = [item.split()[8] for item in GCF]
want=df['Sequence'].unique()
used=[]

with open('filename.csv','r') as f:
    filename = [line.rstrip() for line in f]

with open('GCF_AlkB_cleaned_1_out.faa', "w") as f:
    for name in filename:
        fasta_sequences = SeqIO.parse(open(name),'fasta')
        s = [seq for seq in fasta_sequences]
        for seq in s:
            if (seq.id in want) and (seq.id not in used):
                used.append(seq.id)
                SeqIO.write([seq], f, "fasta")
