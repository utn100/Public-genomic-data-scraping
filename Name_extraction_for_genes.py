import pandas as pd, csv, string, numpy as np
from Bio import SeqIO


with open('RHO_searched_filename.csv','r') as f:
    filenames = [line.rstrip() for line in f]

for filename in filenames:
    print(filename)
    with open(filename,'r') as f:
        sequence = [line.rstrip() for line in f]
    del sequence[0:14]
    threshold_index = [sequence.index(i) for i in sequence if 'threshold' in i][0]
    del sequence[threshold_index:]
    df = pd.DataFrame()
    df['Evalue'] = [float(item.split()[0]) for item in sequence]
    df['Sequence'] = [item.split()[8] for item in sequence]
    searched_sequences = list(df[df['Evalue'] < 0.001]['Sequence'])
    faafile_name='.'.join(filename.split('.')[0:-1])


    with open(faafile_name+'_RHO.faa', "w") as f:
        fasta_sequences = SeqIO.parse(open('/storage/home/utn100/work/IGM_Metagenomes/'+faafile_name),'fasta')
        s = [seq for seq in fasta_sequences]
        for seq in s:
            if seq.id in searched_sequences :
                SeqIO.write([seq], f, "fasta")


