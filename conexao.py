import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")


conexao = psycopg2.connect(database = DB_NAME, host = DB_HOST, user= DB_USER, password = DB_PASS, port = DB_PORT)

cur = conexao.cursor()

cur.execute("""SELECT * FROM public.casos_casos
""")

linha = cur.fetchall()
print(linha[0])
    
cur.close()
conexao.close()