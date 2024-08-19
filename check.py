from Bio import SeqIO

# Função para ler os IDs de um arquivo txt
def read_ids(file_path):
    with open(file_path, 'r') as file:
        ids = [line.strip() for line in file]
    return ids

# Função para verificar a presença dos IDs no arquivo fasta
def check_ids_in_fasta(id_list, fasta_file):
    # Lê os IDs do arquivo fasta
    fasta_ids = set(record.id for record in SeqIO.parse(fasta_file, "fasta"))
    
    # Verifica quais IDs estão presentes e quais estão ausentes
    present_ids = [id for id in id_list if id in fasta_ids]
    absent_ids = [id for id in id_list if id not in fasta_ids]
    
    return present_ids, absent_ids

# Caminhos dos arquivos
id_file = "id.txt"  # arquivo contendo a lista de IDs
input_fasta = "drugs_proteins.fasta"  # arquivo fasta de entrada

# Executando as funções
ids = read_ids(id_file)
present_ids, absent_ids = check_ids_in_fasta(ids, input_fasta)

# Exibindo os resultados
print(f"IDs presentes ({len(present_ids)}): {present_ids}")
print(f"IDs ausentes ({len(absent_ids)}): {absent_ids}")
