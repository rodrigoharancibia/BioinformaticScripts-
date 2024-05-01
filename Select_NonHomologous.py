#Written by: Rodrigo Alex Henríquez Arancibia 
# Date Written: May 1, 2024

from Bio import SeqIO


with open("id.txt","r") as f:
    ids= [line.strip() for line in f]

NonHomologous_file =open("NonHomologous.fasta","w+")# file with Non-homologous protein 


with open("core.fasta", "r") as handle:
  for record in SeqIO.parse(handle,'fasta'): #esse loop vai percorre o arquivo fasta e verificar qual a proteína está presente na planilha de homologos 
    
    if record.id  in ids:
       
         del record 
        
    else:
        SeqIO.write(record ,NonHomologous_file,'fasta')
    
 # Close files 

handle.close()
NonHomologous_file .close()
    

