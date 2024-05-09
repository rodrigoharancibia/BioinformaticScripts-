#Written by: Rodrigo Alex Henríquez Arancibia 
# Date Written: March 2, 2024


from Bio import SeqIO

with open("id.txt","r") as f:# included only the WP code, excluded the protein and species name: ex-WP_005513056.1
  ids= [line.strip() for line in f]

'''
 for id in ids:
     print(id)
'''
 
  
  #Open
protein_fasta_handle = open("core.fasta","r")
selected_proteins= open("output.fasta","w")
'''
 # include proteins in the new file 
for record in SeqIO.parse(protein_fasta_handle, "fasta"):
    if record.id in  ids:
        SeqIO.write(record,selected_proteins, "fasta")
    else :
       pass
    # Not include  proteins in the new file 

    '''
for record in SeqIO.parse(protein_fasta_handle, "fasta"):
      if record.id in ids:
          continue
      else :
       SeqIO.write(record,selected_proteins, "fasta")
    
  



















    
protein_fasta_handle.close()
selected_proteins.close()