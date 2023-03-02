import psycopg2
import pandas as pd


#conectar ao banco
conn = psycopg2.connect(
   database="testes_db", user='postgres', password='2809', host='localhost', port= '5432'
)


def listar(veiculos):
    cursor = conn.cursor()
    SQL = " SELECT * FROM VEICULOS "
    reg = SQL
    cursor.execute(SQL)
    registros = []
    registros.append(SQL)
    registros = cursor.fetchall()
    for reg in registros:
        df = pd.DataFrame([reg], columns=['id', 'nome','placa','anofab','fabricante','datacad'])
        df.head(2)
        print(reg)
        conn.close()


#==================================
#def listar(veiculos):
#    placa = input('Informe a placa do veículo desejado: ')
#    cursor = conn.cursor()
#    SQL = " SELECT * FROM VEICULOS WHERE PLACA = '" + placa + "'"
#    cursor.execute(SQL)
#    registros = cursor.fetchall()
#    print(registros)
#    veiculos.append((placa))