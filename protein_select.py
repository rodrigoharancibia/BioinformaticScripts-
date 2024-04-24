
#Written by: Rodrigo Alex Henríquez Arancibia 
# Date Written: March 2, 2024


from Bio import SeqIO

with open("IDS.txt","r") as f: 
  ids= [line.strip() for line in f]

  """
  for id in ids:
     print(id)
  """
  #Open
protein_fasta_handle = open("core.fasta","r")
selected_proteins= open("target_proteins.fasta","w")


for record in SeqIO.parse(protein_fasta_handle, "fasta"):
    if record.id in ids:
        SeqIO.write(record,selected_proteins, "fasta")

protein_fasta_handle.close()
selected_proteins.close()
