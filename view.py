import sqlite3 as lite

con = lite.connect('dados.db')

#Inserir gategoria

def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Categoria (nome) VALUES(?)"
        cur.execute(query,i)

#Inserir Receitas

def inserir_receitas(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Receitas (categoria, adicionado_em, valor) VALUES(?,?,?)"
        cur.execute(query,i)

#Inserir Despesas

def inserir_despesas(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Despesas (categoria, retirado_em, valor) VALUES(?,?,?)"
        cur.execute(query,i)


#Funcoes para deletar ----------------------------------

#deletar receitas
def deletar_receitas(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Receitas WHERE id=?"
        cur.execute(query,i)

def deletar_despesas(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Despesas WHERE id=?"
        cur.execute(query,i)

#Funcoes para ver dados --------------------------

#Ver Categoria
def ver_categoria():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Categoria')
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens

#print(ver_categoria())

#Ver Receitas
def ver_receitas():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Receitas')
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens

#Ver Despesas
def ver_despesas():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Despesas')
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens