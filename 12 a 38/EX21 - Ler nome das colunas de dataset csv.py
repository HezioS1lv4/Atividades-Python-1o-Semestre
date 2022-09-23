# Hézio

import csv

with open('stratospheric-ozone-concentration.csv') as arquivo:
    leitor = csv.reader(arquivo, delimiter=',')
    print(f"As colunas são: {next(leitor)}")
