import pandas as pd, csv, string, numpy as np


with open('RHO_searched_filename.csv','r') as f:
    filenames = [line.rstrip() for line in f]

count=[]
faafile_names=[]

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
        count.append(len(searched_sequences))
        faafile_names.append('.'.join(filename.split('.')[0:-1]))
        
newdf = pd.DataFrame()
newdf['filename'] = faafile_names
newdf['count'] = count
newdf.to_csv('RHO_genecount.csv')

