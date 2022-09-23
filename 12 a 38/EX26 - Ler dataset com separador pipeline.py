# Hézio

import csv

with open("Notas.csv", 'r', encoding='UTF8', newline='') as f:
    reader = csv.reader(f, delimiter='|')
    for row in reader:
        print(row)
