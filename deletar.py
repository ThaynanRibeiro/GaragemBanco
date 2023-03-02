import psycopg2

conn = psycopg2.connect(
   database="testes_db", user='postgres', password='2809', host='localhost', port= '5432'
)
conn.autocommit = True
cursor = conn.cursor()

cursor.execute('''DELETE FROM VEICULOS ''')
       