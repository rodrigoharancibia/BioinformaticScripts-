#Written by: Rodrigo Alex Henríquez Arancibia 
# Date Written: March 2, 2024


from Bio import SeqIO
with open("vaxign.txt","r") as f: # estamos inserindo o arquivo txt no código, coloque o nome do arquivo que você criou
  ids= [line.strip() for line in f]



protein_fasta_handle = open("TM_Porteins_selected_outer_membrane.fasta","r") # inserimos o arquivo fasta
selected_proteins= open("output.fasta","w") # Aqui criamos a nova sequência fasta


for record in SeqIO.parse(protein_fasta_handle, "fasta"): # Aqui se faz a seleção das proteínas
    if record.id in  ids:
        SeqIO.write(record,selected_proteins, "fasta")
    else :
       pass

protein_fasta_handle.close()
selected_proteins.close()
