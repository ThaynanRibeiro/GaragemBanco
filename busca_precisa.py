import psycopg2
import pandas as pd

#conectar ao banco
conn = psycopg2.connect(
   database="testes_db", user='postgres', password='2809', host='localhost', port= '5432'
)

def busca_precisa(veiculos):
    while True:
        print('''\n\033[1m\033[33mEscolha uma opção:\033[0;0m
        
        [1] Nome
        [2] Placa
        [3] Ano de Fabricação
        [4] Fabricante
        [5] Data do Cadastro
        ''')
        opcao = int(input('Opção: '))
        if opcao == 1:
            busca_nome(veiculos)
        elif opcao == 2:
            busca_placa(veiculos)
        elif opcao == 3:
            busca_anofab(veiculos)
        elif opcao == 4:
            busca_fabricante(veiculos)
        elif opcao == 5:
            busca_datacad(veiculos)
        else:
            print('\033[0;31mDigite uma opção válida!\033[m')
            sleep(1)