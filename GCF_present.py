import pandas as pd
import numpy as np
import string, csv
import pyfasta
from pyfasta import Fasta

GCF = pd.read_csv('GCF_hmm_table.csv')
seq=GCF[GCF['E-value']<0.01]['Sequence'].unique()

name = []
present = []
GCF_present = pd.DataFrame()
with open('filename.csv','r') as f:
    filename = [line.rstrip() for line in f]

for f in filename:
    fa = Fasta(f)
    headseq = [item.split()[0] for item in fa.keys()]
    presentseq = [item for item in headseq if item in seq]
    name.append('GCA_'+f.split('_')[1])
    if len(presentseq) == 0:
        present.append('NA')
    else:
        present.append(','.join(presentseq))

GCF_present['name'] = name
GCF_present['present_absent'] = present

GCF_present.to_csv('GCF_present.csv')

