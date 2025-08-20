import sqlite3

conn = sqlite3.connect("estoque.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM produtos")
produtos = cursor.fetchall()

if produtos:
    for produto in produtos:
        print(produto)
else:
    print("Nenhum produto cadastrado ainda.")

conn.close()