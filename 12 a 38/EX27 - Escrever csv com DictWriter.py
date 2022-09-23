# Hézio

import csv

meu_dict = {
    "key1": "valor_a",
    "key2": "valor_b",
    "key3": "valor_c"
}

with open("Dicionario.csv", 'w', encoding='UTF8', newline='') as novo_arquivo:
    writer = csv.writer(novo_arquivo)
    for key, value in meu_dict.items():
        writer.writerow([key, value])
