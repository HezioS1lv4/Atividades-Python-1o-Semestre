# Hézio

import csv
import pandas as pd

class Brinquedo:
    def __init__(self, Number, City, Gender, Age, Income, Illness):
        self.Number = Number
        self.City = City
        self.Gender = Gender
        self.Age = Age
        self.Income = Income
        self.Illness = Illness

    def __str__(self):
        return f"Brinquedo {self.Number}: {self.City}, {self.Gender}, {self.Age}, {self.Income}, {self.Illness} "


lista_brinquedo = []

with open('toy_dataset.csv') as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor, None)
    for Number, City, Gender, Age, Income, Illness in leitor:
        Age = int(Age)
        Income = float(Income)
        lista_brinquedo.append(Brinquedo(Number, City, Gender, Age, Income, Illness))

    for Brinquedo in lista_brinquedo:
        print(Brinquedo)
