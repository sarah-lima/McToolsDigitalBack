import requests;
import json;

def get():
    r = requests.get('https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json&dataInicial=01/01/2000&dataFinal=31/12/2100')
    dict_r = r.json()
    return dict(data=dict_r)
