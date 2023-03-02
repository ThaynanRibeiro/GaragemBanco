import requests
import json
import pandas as pd
import psycopg2


  # Função para criar conexão no banco
def conecta_db():
  con = psycopg2.connect(host='localhost', 
                         database='testes_db',
                         user='postgre', 
                         password='2809')
  return con
  # Função para criar tabela no banco
def criar_db(sql):
  con = conecta_db()
  cur = con.cursor()
  cur.execute(sql)
  con.commit()
  con.close()
  # Dropando a tabela caso ela já exista
sql = 'DROP TABLE IF EXISTS public.deputados'
criar_db(sql)
# Criando as tabelas
sql = '''CREATE TABLE public.deputados 
      ( id            character varying(10), 
        nome          character varying(500), 

      )'''