from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

#Função para conectar ao banco
def get_db_connection():
    conn = sqlite3.connect("estoque.db")
    conn.row_factory = sqlite3.Row
    return conn

#Criar tabela se não existir
def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

# Rota principal - lista produtos
@app.route("/")
def index():
    conn = get_db_connection()
    produtos = conn.execute("SELECT* FROM produtos").fetchall()
    conn.close()
    return render_template("index.html", produtos=produtos)

# Adicionar produto
@app.route("/add", methods=("GET", "POST"))
def add():
    if request.method == "POST":
        nome = request.form["nome"]
        quantidade = request.form["quantidade"]

        conn = get_db_connection()
        conn.execute("INSERT INTO produtos (nome, quantidade) VALUES (?, ?)",
                     (nome, quantidade))
        conn.commit()
        conn.close()
        return redirect("/")
    return render_template("add.html")

#Deletar produto
@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM produtos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)