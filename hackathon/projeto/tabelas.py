import sqlite3

conexao = sqlite3.connect('SAI.db')
cursor = conexao.cursor()

def criar_tabelas():
    conn = sqlite3.connect('SAI.db')
    cursor = conn.cursor()

    # Tabelas para cada tipo de reclamação
    tabelas = [
        'CREATE TABLE IF NOT EXISTS vazamento_agua ('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'cep TEXT,'
        'numero_residencia TEXT,'
        'uf TEXT,'
        'cidade TEXT,'
        'bairro TEXT,'
        'logradouro TEXT,'
        'FOREIGN KEY (CPF) REFERENCES usuarios(CPF))',

        'CREATE TABLE IF NOT EXISTS esgoto_ceu_aberto ('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'cep TEXT,'
        'numero_residencia TEXT,'
        'uf TEXT,'
        'cidade TEXT,'
        'bairro TEXT,'
        'logradouro TEXT,'
        'FOREIGN KEY (CPF) REFERENCES usuarios(CPF))',

        'CREATE TABLE IF NOT EXISTS buracos_via ('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'cep TEXT,'
        'numero_residencia TEXT,'
        'uf TEXT,'
        'cidade TEXT,'
        'bairro TEXT,'
        'logradouro TEXT,'
        'FOREIGN KEY (CPF) REFERENCES usuarios(CPF))',

        'CREATE TABLE IF NOT EXISTS furto_energia ('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'cep TEXT,'
        'numero_residencia TEXT,'
        'uf TEXT,'
        'cidade TEXT,'
        'bairro TEXT,'
        'logradouro TEXT,'
        'FOREIGN KEY (CPF) REFERENCES usuarios(CPF))',

        'CREATE TABLE IF NOT EXISTS fiacao_eletrica_rompida ('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'cep TEXT,'
        'numero_residencia TEXT,'
        'uf TEXT,'
        'cidade TEXT,'
        'bairro TEXT,'
        'logradouro TEXT,'
        'FOREIGN KEY (CPF) REFERENCES usuarios(CPF))',

        'CREATE TABLE IF NOT EXISTS lixo_acumulado ('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'cep TEXT,'
        'numero_residencia TEXT,'
        'uf TEXT,'
        'cidade TEXT,'
        'bairro TEXT,'
        'logradouro TEXT,'
        'FOREIGN KEY (CPF) REFERENCES usuarios(CPF))',

        'CREATE TABLE IF NOT EXISTS poda_arvores ('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'cep TEXT,'
        'numero_residencia TEXT,'
        'uf TEXT,'
        'cidade TEXT,'
        'bairro TEXT,'
        'logradouro TEXT,'
        'FOREIGN KEY (CPF) REFERENCES usuarios(CPF))',

        'CREATE TABLE IF NOT EXISTS troca_lampada ('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'cep TEXT,'
        'numero_residencia TEXT,'
        'uf TEXT,'
        'cidade TEXT,'
        'bairro TEXT,'
        'logradouro TEXT,'
        'FOREIGN KEY (CPF) REFERENCES usuarios(CPF))'
    ]

    for tabela in tabelas:
        cursor.execute(tabela)

    conn.commit()
    conn.close()