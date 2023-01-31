import requests
from math import sin, cos, sqrt, atan2, radians
import pandas as pd
from time import sleep
import json


def save_dict_to_json(dictionary, file_name):
    with open(file_name, "w") as file:
        json.dump(dictionary, file)


def load_json_to_dict(file_name):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        return {}


buscas = load_json_to_dict('dados.json')


# procurado = []

def coordenadas_cep(cep):
    try:
        cep = str(cep)

        if not buscas.get(cep) is None:
            return buscas[cep]
        else:
            url = "https://www.cepaberto.com/api/v3/cep?cep=" + cep
            # O seu token está visível apenas pra você
            headers = {'Insira seu token aqui, para obter um token você deve se cadastrar na api do cepaberto'}
            sleep(1.5)
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                final = response.json()

                latitude = final['latitude']
                longitude = final['longitude']

                buscas[cep] = [latitude, longitude]
                save_dict_to_json(buscas, 'dados.json')
                return buscas[cep]
            raise ('ERROR AO CARREGAR A PAGINA')
    except:
        return 'não encontrado'


def distance_haversine(cordenadas1, cordenadas2):
    lat1 = float(cordenadas1[0])
    lon1 = float(cordenadas1[1])

    lat2 = float(cordenadas2[0])
    lon2 = float(cordenadas2[1])

    R = 6371.0  # raio da Terra em quilômetros
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance  # em km


def calcular_distancia(cep1, cep2):
    try:

        cordenada1 = coordenadas_cep(cep1)
        cordenada2 = coordenadas_cep(cep2)
        resultado = distance_haversine(cordenada1, cordenada2)
        return resultado
    except:
        return 'sem calculo'
