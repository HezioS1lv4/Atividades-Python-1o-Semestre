# Hézio

import csv

with open('Dicionario.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    mydict = dict(reader)
    print(mydict)