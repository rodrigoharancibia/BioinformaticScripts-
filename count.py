
#Written by: Rodrigo Alex Henríquez Arancibia 
# Date Written: August 10, 2023

from Bio import SeqIO 

file = open('Nonhomologous.fasta','r+') # insere o arquivo no script 
deleted_proteins =open('deleted.txt','w+')# insere o arquivo para registrar as proteínas deletadas
size_proteins=open('lenght_proteins.txt','w+') # insere o arquivo para mostra o tamanho das proteínas 
proteins =open('proteins_size.txt','w+') # insere o arquivo com as proteínas selecionadas 


for seq_record in SeqIO.parse(file,'fasta'): # esse loop anotar o ID da proteína e conta o número de  aa
    
    print(seq_record.id,':',len(seq_record),file= size_proteins)
   
    if len(seq_record)<100:
        SeqIO.write(seq_record ,deleted_proteins,'fasta')
        del seq_record

    
   
    
    else:
     SeqIO.write(seq_record ,proteins ,'fasta')
    
    
