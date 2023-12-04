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
        if valor != "Desconhecido":
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

#cria um vetor dinamico similaridade_local
similaridade_local = {}
cur = conexao.cursor()
for key in novo_caso:
    similaridade_local[key] = {}
    # SELECT key FROM public.casos_casos
    cur.execute(f"SELECT {key} FROM public.casos_casospt")
    # Armazena os valores
    antigo_caso_str = cur.fetchall()

    
    valor_maximo_var = valor_maximo(similaridade, key)
    valor_minimo_var = valor_minimo(similaridade, key)
    for i in range(0, len(antigo_caso_str)):
        if antigo_caso_str[i][0] == None:
            antigo_caso_str[i] = ("Desconhecido",)
        antigo_caso_int = similaridade[key][antigo_caso_str[i][0]]
        # Adiciona em um vetor os valores de similaridade local
        similaridade_local[key][i+1] = (calculo_similaridade_local(novo_caso, similaridade, key, antigo_caso_int, valor_maximo_var, valor_minimo_var))

cur.close()
conexao.close()





    

    