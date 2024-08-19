#Written by: Rodrigo Alex Henríquez Arancibia 
# Date Written: May 1, 2024

from Bio import SeqIO


with open("prot.txt","r") as f:
    ids= [line.strip() for line in f]

NonHomologous_file =open("Nonhomologous.fasta","w+")# file with Non-homologous protein 
#Homologous_file= open("Homologous.fasta","w+")

with open("corecompletegenomes.faa", "r") as h:
  for record  in SeqIO.parse(h,"fasta"): #esse loop vai percorre o arquivo fasta e verificar qual a proteína está presente na planilha de homologos 
    
    if record.id   not in ids:
       
        SeqIO.write(record,NonHomologous_file, "fasta")

  else:
       pass
    

    
          
        
    
 # Close files 

h.close()
NonHomologous_file.close()
    

