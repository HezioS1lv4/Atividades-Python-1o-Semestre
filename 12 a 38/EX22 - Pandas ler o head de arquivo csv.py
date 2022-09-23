# Hézio

import pandas as pd
import csv

with open('stratospheric-ozone-concentration.csv') as arquivo:
    df = pd.DataFrame(arquivo)
    print(df.head())