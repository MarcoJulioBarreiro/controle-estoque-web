import sqlite3

conn = sqlite3.connect("estoque.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute("SELECT * FROM produtos")
produtos = cursor.fetchall()

for p in produtos:
    print(p['nome'], p['quantidade'])

conn.close()