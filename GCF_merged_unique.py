import pandas as pd
import numpy as np
from Bio import SeqIO
import string,csv

with open('unique.csv','r') as f:
    usedid = [line.rstrip() for line in f]

use = [item.split()[0][1:] for item in usedid]

with open('filename.csv','r') as f:
    filename = [line.rstrip() for line in f]

file_GCF = [item for item in filename if 'GCF' in item]

with open('GCF_merged_unique_1.faa', "w") as f:
    for name in file_GCF[6900:7000]:
        print(file_GCF.index(name))
        fasta_sequences = SeqIO.parse(open(name),'fasta')
        s = [seq for seq in fasta_sequences]
        for seq in s:
            if seq.id not in use:
                use.append(seq.id)
                SeqIO.write([seq], f, "fasta")


