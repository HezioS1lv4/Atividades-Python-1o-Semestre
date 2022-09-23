# Hézio

import csv

with open ('titles.csv') as csv_file:
    arquivo = csv.reader(csv_file, delimiter=',')
    contagem_linha = 0
    for linha in arquivo:
        if contagem_linha == 0:
            print(f'As colunas são: {",".join(linha)}')
            contagem_linha += 1
        else:
            print(f'Linha {contagem_linha}: ID: {linha[0]}; Titulo: {linha[1]}; Tipo: {linha[3]}; Descrição: {linha[4]}; Ano_de_lancamento: {linha[5]}; Generos: {linha[6]}')
            contagem_linha += 1