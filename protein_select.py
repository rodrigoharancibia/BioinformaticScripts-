#Written by: Rodrigo Alex Henríquez Arancibia 
# Date Written: March 2, 2024


from Bio import SeqIO

import re


with open("pbit.txt","r") as f:
    ids= [line.strip() for line in f]





protein_fasta_handle = open("cytoplasmatic.faa","r") 
  
selected_proteins =  open ("drugt_proteins_target.faa", "w") 

for record in SeqIO.parse(protein_fasta_handle, "fasta"): 
        if record.id in  ids:
            SeqIO.write(record,selected_proteins, "fasta")
        else :
            pass
