import sqlite3
import requests

# Função para criar tabelas no banco de dados
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
tabelasdb = criar_tabelas()
# Função para inserir reclamação
def inserir_reclamacao(tipo_reclamacao, cpf, cep, numero_residencia, uf, cidade, bairro, logradouro):
    conn = sqlite3.connect('SAI.db')
    cursor = conn.cursor()

    tabela_reclamacao = {
        '1': 'vazamento_agua',
        '2': 'esgoto_ceu_aberto',
        '3': 'buracos_via',
        '4': 'furto_energia',
        '5': 'fiacao_eletrica_rompida',
        '6': 'lixo_acumulado',
        '7': 'poda_arvores',
        '8': 'troca_lampada'
    }

    # Verifica se o tipo de reclamação é válido
    if tipo_reclamacao not in tabela_reclamacao:
        print("Tipo de reclamação inválido!")
        return

    tabela = tabela_reclamacao[tipo_reclamacao]

    # Inserção na tabela correspondente ao tipo de reclamação
    try:
        cursor.execute(
            f'INSERT INTO {tabela} (CPF, cep, numero_residencia, uf, cidade, bairro, logradouro) VALUES (?, ?, ?, ?, ?, ?, ?)',
            (cpf, cep, numero_residencia, uf, cidade, bairro, logradouro)
        )
        conn.commit()
        print("Reclamação registrada com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao inserir reclamação: {e}")

    conn.close()
reclamacoes = inserir_reclamacao