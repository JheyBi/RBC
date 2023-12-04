import psycopg2
import os
from dotenv import load_dotenv
import json
from random import randint

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")


conexao = psycopg2.connect(database = DB_NAME, host = DB_HOST, user= DB_USER, password = DB_PASS, port = DB_PORT)

# cur = conexao.cursor()
# for key in novo_caso:
#     # SELECT key FROM public.casos_casos
#     cur.execute(f"SELECT {key} FROM public.casos_casos")
#     # Armazena os valores
#     antigo_caso_str = cur.fetchall()
# cur.close()
# conexao.close()


with open('novo_caso.json', 'r') as f:
    novo_caso = json.load(f)


with open('similaridade.json', 'r') as f:
    similaridade = json.load(f)


def valor_maximo(similaridade, key):
    maximo = 0
    for valor in similaridade[key]:
        if similaridade[key][valor] > maximo:
            maximo = similaridade[key][valor]
    return maximo

def valor_minimo(similaridade, key):
    minimo = 100
    for valor in similaridade[key]:
        if similaridade[key][valor] < minimo:
            minimo = similaridade[key][valor]
    return minimo


def calculo_similaridade_local(novo_caso, similaridade, key, antigo_caso,valor_maximo, valor_minimo):
    return 1-(abs(similaridade[key][novo_caso[key]]-antigo_caso)/(valor_maximo-valor_minimo))


#Exemplo de como é para ficar o calculo da similiridade local
# for i in range(0, 5):
#     novo_caso_var = 57
#     antigo_caso = [100,90,30,45,73]
#     valor_maximo = max(antigo_caso)
#     valor_minimo = min(antigo_caso)
#     print(1-(abs(novo_caso_var-antigo_caso[i])/(valor_maximo-valor_minimo)))

similaridade_local = {}
for key in novo_caso:
    # SELECT key FROM public.casos_casos
    cur = conexao.cursor()
    cur.execute(f"SELECT {key} FROM public.casos_casos")
    # Armazena os valores
    antigo_caso_str = cur.fetchall()
    cur.close()
    conexao.close()
    valor_maximo = valor_maximo(similaridade, key)
    valor_minimo = valor_minimo(similaridade, key)
    for i in range(0, len(antigo_caso_str)):
        # Adiciona em um vetor os valores de similaridade local
        antigo_caso_int = similaridade[key][antigo_caso_str[i][0]]
        similaridade_local[key][i] = calculo_similaridade_local(novo_caso, similaridade, key, antigo_caso_int, valor_maximo, valor_minimo)
    break


    

    