from dependencias import calcular_distancia
from time import sleep
import pandas as pd
import openpyxl

df = pd.read_excel("CEP-DIST.xlsx")

distancias = []   #Coluna a ser adicionada ao dataframe

max = len(df)
for i in range(len(df)):
    sleep(1)
    cep1 = df["CEP Rem."][i].replace('-', '')
    if df["CEP Receb."][i] == "00000-000":
        cep2 = df["CEP Dest."][i].replace('-', '')
    else:
        cep2 = df["CEP Receb."][i].replace('-', '')

    distancia = calcular_distancia(cep1, cep2)
    print(distancia, round((i/max)*100, 2))

    distancias.append(distancia)

df['Distancia'] = distancias
df.to_excel('CEP-DIST-WDISTANCE.xlsx')