import pandas as pd
import json


def create_file_excel(data, title='static/data_bcb.xlsx'):
    dados = []
    for item in data:
        dados.append(list(item))
    df = pd.DataFrame(dados,
                      columns=['data', 'valor'])

    df.to_excel(title, sheet_name='dados')
    
    
def create_file_json(dictionary):
    dados = []
    for item in dictionary:
        dados.append(list(item))
        
    for subitem in dados:
        subitem[0] = str(subitem[0]) 
    with open("static/data_bcb.json", "w") as outfile: 
        json.dump({'data':dados}, outfile) 
