# Hézio

import csv

header = ["Nome", "Idade", "Nota", "Menção"]
data1 = ["Guilherme", 19, 8.5, "MS"]
data2 = ["Daniel", 21, 7.3, "MM"]
data3 = ["Felipe", 18, 10, "SS"]
data4 = ["Ian", 25, 5.4, "MI"]
data5 = ["Pedro", 20, 0.0, "II"]

cont = 1

with open("Notas.csv", 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data1)
    writer.writerow(data2)
    writer.writerow(data3)
    writer.writerow(data4)
    writer.writerow(data5)
