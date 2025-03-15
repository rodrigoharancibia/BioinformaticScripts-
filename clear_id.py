import re 
# Abre o arquivo de entrada para leitura
with open("id.txt", "r") as proteins:
    ids = proteins.readlines()



# Processa cada linha

clear = [re.sub(r"^(WP_\d+\.\d+).*", r"\1", id.strip()) for id  in ids]



# Salva o resultado em um novo arquivo
with open("wp.txt", "w") as output:
    for c in clear:
        output.write(c + "\n")       