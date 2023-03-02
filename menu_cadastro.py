import psycopg2
import pandas as pd
import functools
from time import sleep
from datetime import date


#conectar ao banco
conn = psycopg2.connect(
   database="testes_db", user='postgres', password='2809', host='localhost', port= '5432'
)
conn.autocommit = True
cursor = conn.cursor()

def exibir_menu():
    print('''\n\033[1m\033[33mEscolha uma opção:\033[0;0m

    [1] Cadastrar um veículo
    [2] Veículos ativos no sistema
    [3] Pesquisa precisa
    [4] Desativar veículo
    [5] Finalizar programa
    ''')

def main():
    veiculos = []
    while True:
        exibir_menu()
        opcao = int(input('Opção: '))
        if opcao == 1:
            cadastrar(veiculos)
        elif opcao == 2:
            listar(veiculos)
        elif opcao == 3:
            busca_precisa(veiculos)
        elif opcao == 4:
            desativar(veiculos)
            print('\n\033[32mVeículo Desabilitado\033[0;0m')
        elif opcao == 5:
            print('\n\033[0;31mPrograma Finalizado!\033[m\n\n\n') 
            sleep(1)
            exit()
        else:
            print('\033[0;31mDigite uma opção válida!\033[m')
            sleep(1)

def cadastrar(veiculos):
    nome = input('Informe o nome do veículo: ')
    placa = input('Placa: ')
    anofab = input('Ano de fabricação: ')
    fabricante = input('Fabricante do veiculo: ')
    veiculos.append((nome,placa,anofab,fabricante))
    cursor.execute("INSERT INTO VEICULOS (NOME,PLACA,ANOFAB,FABRICANTE,STATUS) VALUES ('"+nome+"','"+placa+"',"+anofab+",'"+fabricante+"','Ativo')")

def listar(veiculos):
    cursor = conn.cursor()
    SQL = " SELECT * FROM VEICULOS WHERE STATUS <> 'DESABILITADO'"
    reg = SQL
    cursor.execute(SQL)
    registros = []
    registros.append(SQL)
    registros = cursor.fetchall()
    for reg in registros:
        df = pd.DataFrame([reg], columns=['id', 'nome','placa','anofab','fabricante','datacad','status'])
        df.head()
        print(reg)
        conn.close()

def busca_precisa(veiculos):
    while True:
        print('''\n\033[1m\033[33mEscolha uma opção:\033[0;0m
        
        [1] Nome
        [2] Placa
        [3] Ano de Fabricação
        [4] Fabricante
        [5] Data do Cadastro
        [6] Menu Anterior
        [7] Finalizar programa
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
        elif opcao == 6:
            return main
        elif opcao == 7:
            print('\n\033[0;31mPrograma Finalizado!\033[m\n\n\n') 
            sleep(1)
            exit()
        else:
            print('\033[0;31mDigite uma opção válida!\033[m')
            sleep(1)

def busca_nome(veiculos):
    nome = (input('Nome: '))
    cursor = conn.cursor()
    SQL = " SELECT * FROM VEICULOS WHERE STATUS <> 'DESABILITADO' AND NOME LIKE '%"+nome+"%';"
    reg = SQL
    cursor.execute(SQL)
    registros = []
    registros.append(SQL)
    registros = cursor.fetchall()
    for reg in registros:
        df = pd.DataFrame([reg], columns=['id', 'nome','placa','anofab','fabricante','datacad','status'])
        df.head()
        print(reg)
        conn.close()

def busca_placa(veiculos):
    placa = (input('Placa: '))
    cursor = conn.cursor()
    SQL = " SELECT * FROM VEICULOS WHERE STATUS <> 'DESABILITADO' AND PLACA = '"+placa+"';"
    reg = SQL
    cursor.execute(SQL)
    registros = []
    registros.append(SQL)
    registros = cursor.fetchall()
    for reg in registros:
        df = pd.DataFrame([reg], columns=['id', 'nome','placa','anofab','fabricante','datacad','status'])
        df.head()
        print(reg)
        conn.close()

def busca_anofab(veiculos):
    anofab = (input('Ano de Fabricação: '))
    cursor = conn.cursor()
    SQL = " SELECT * FROM VEICULOS WHERE STATUS <> 'DESABILITADO' AND ANOFAB = '"+anofab+"';"
    reg = SQL
    cursor.execute(SQL)
    registros = []
    registros.append(SQL)
    registros = cursor.fetchall()
    for reg in registros:
        df = pd.DataFrame([reg], columns=['id', 'nome','placa','anofab','fabricante','datacad','status'])
        df.head()
        print(reg)
        conn.close()

def busca_fabricante(veiculos):
    fabricante = (input('Fabricante: '))
    cursor = conn.cursor()
    SQL = " SELECT * FROM VEICULOS WHERE STATUS <> 'DESABILITADO' AND FABRICANTE = '"+fabricante+"';"
    reg = SQL
    cursor.execute(SQL)
    registros = []
    registros.append(SQL)
    registros = cursor.fetchall()
    for reg in registros:
        df = pd.DataFrame([reg], columns=['id', 'nome','placa','anofab','fabricante','datacad','status'])
        df.head()
        print(reg)
        conn.close()

def busca_datacad(veiculos):
    datacad = (input('Data de Cadastro: '))
    cursor = conn.cursor()
    SQL = " SELECT * FROM VEICULOS WHERE STATUS <> 'DESABILITADO' AND DATACAD = '"+datacad+"';"
    reg = SQL
    cursor.execute(SQL)
    registros = []
    registros.append(SQL)
    registros = cursor.fetchall()
    for reg in registros:
        df = pd.DataFrame([reg], columns=['id', 'nome','placa','anofab','fabricante','datacad','status'])
        df.head()
        print(reg)
        conn.close()
def desativar(veiculos):
    placa = input('Placa: ')
    cursor.execute("UPDATE VEICULOS SET STATUS='Desabilitado' WHERE PLACA='"+placa+"';")
main()

   