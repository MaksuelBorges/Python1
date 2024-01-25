import sqlite3
import requests


def criar_tabelas():
    conn = sqlite3.connect('SAI.db')
    cursor = conn.cursor()

    # Tabelas para cada tipo de reclamação
    tabelas = [
        'CREATE TABLE IF NOT EXISTS vazamento_agua (tipo_reclamacao TEXT, cpf INTEGER, cep TEXT, numero_residencia TEXT, uf TEXT, cidade TEXT, bairro TEXT, logradouro TEXT, FOREIGN KEY (cpf) REFERENCES usuarios(cpf))',
        'CREATE TABLE IF NOT EXISTS esgoto_ceu_aberto (tipo_reclamacao TEXT, cpf INTEGER, cep TEXT, numero_residencia TEXT, uf TEXT, cidade TEXT, bairro TEXT, logradouro TEXT, FOREIGN KEY (cpf) REFERENCES usuarios(cpf))',
        'CREATE TABLE IF NOT EXISTS buracos_via (tipo_reclamacao TEXT, cpf INTEGER, cep TEXT, numero_residencia TEXT, uf TEXT, cidade TEXT, bairro TEXT, logradouro TEXT, FOREIGN KEY (cpf) REFERENCES usuarios(cpf))',
        'CREATE TABLE IF NOT EXISTS furto_energia (tipo_reclamacao TEXT, cpf INTEGER, cep TEXT, numero_residencia TEXT, uf TEXT, cidade TEXT, bairro TEXT, logradouro TEXT, FOREIGN KEY (cpf) REFERENCES usuarios(cpf))',
        'CREATE TABLE IF NOT EXISTS fiacao_eletrica_rompida (tipo_reclamacao TEXT, cpf INTEGER, cep TEXT, numero_residencia TEXT, uf TEXT, cidade TEXT, bairro TEXT, logradouro TEXT, FOREIGN KEY (cpf) REFERENCES usuarios(cpf))',
        'CREATE TABLE IF NOT EXISTS lixo_acumulado (tipo_reclamacao TEXT, cpf INTEGER, cep TEXT, numero_residencia TEXT, uf TEXT, cidade TEXT, bairro TEXT, logradouro TEXT, FOREIGN KEY (cpf) REFERENCES usuarios(cpf))',
        'CREATE TABLE IF NOT EXISTS poda_arvores (tipo_reclamacao TEXT, cpf INTEGER, cep TEXT, numero_residencia TEXT, uf TEXT, cidade TEXT, bairro TEXT, logradouro TEXT, FOREIGN KEY (cpf) REFERENCES usuarios(cpf))',
        'CREATE TABLE IF NOT EXISTS troca_lampada (tipo_reclamacao TEXT, cpf INTEGER, cep TEXT, numero_residencia TEXT, uf TEXT, cidade TEXT, bairro TEXT, logradouro TEXT, FOREIGN KEY (cpf) REFERENCES usuarios(cpf))'
    ]

    for tabela in tabelas:
        cursor.execute(tabela)

    conn.commit()
    conn.close()

def inserir_reclamacao(tipo_reclamacao, cpf, cep, numero_residencia, uf, cidade, bairro, logradouro):
    conn = sqlite3.connect('SAI.db')
    cursor = conn.cursor()

    # Inserir na tabela correspondente ao tipo de reclamação
    if tipo_reclamacao == '1':
        cursor.execute(
            'INSERT INTO vazamento_agua (tipo_reclamacao, cpf, cep, numero_residencia, uf, cidade, bairro, logradouro) VALUES (?, ?, ?, ?, ?, ?, ?,?)',
            ('vazamento de agua',cpf_logado, cep, numero_residencia, uf, cidade, bairro, logradouro))
    elif tipo_reclamacao == '2':
        cursor.execute(
            'INSERT INTO esgoto_ceu_aberto (tipo_reclamacao, cpf, cep, numero_residencia, uf, cidade, bairro, logradouro) VALUES (?, ?, ?, ?, ?, ?, ?,?)',
            ('esgoto a ceu aberto',cpf_logado, cep, numero_residencia, uf, cidade, bairro, logradouro))
    elif tipo_reclamacao == '3':
        cursor.execute(
            'INSERT INTO buracos_via (tipo_reclamacao, cpf, cep, numero_residencia, uf, cidade, bairro, logradouro) VALUES (?, ?, ?, ?, ?, ?, ?,?)',
            ('buracos na via',cpf_logado, cep, numero_residencia, uf, cidade, bairro, logradouro))
    elif tipo_reclamacao == '4':
        cursor.execute(
            'INSERT INTO furto_energia (tipo_reclamacao, cpf, cep, numero_residencia, uf, cidade, bairro, logradouro) VALUES (?, ?, ?, ?, ?, ?, ?,?)',
            ('furto de energia',cpf_logado, cep, numero_residencia, uf, cidade, bairro, logradouro))
    elif tipo_reclamacao == '5':
        cursor.execute(
            'INSERT INTO fiacao_eletrica_rompida (tipo_reclamacao, cpf, cep, numero_residencia, uf, cidade, bairro, logradouro) VALUES (?, ?, ?, ?, ?, ?, ?,?)',
            ('fiação eletrica rompida',cpf_logado, cep, numero_residencia, uf, cidade, bairro, logradouro))
    elif tipo_reclamacao == '6':
        cursor.execute(
            'INSERT INTO lixo_acumulado (tipo_reclamacao, cpf, cep, numero_residencia, uf, cidade, bairro, logradouro) VALUES (?, ?, ?, ?, ?, ?, ?,?)',
            ('lixo acumulado',cpf_logado, cep, numero_residencia, uf, cidade, bairro, logradouro))
    elif tipo_reclamacao == '7':
        cursor.execute(
            'INSERT INTO poda_arvores (tipo_reclamacao, cpf, cep, numero_residencia, uf, cidade, bairro, logradouro) VALUES (?, ?, ?, ?, ?, ?, ?,?)',
            ('poda de arvores',cpf_logado, cep, numero_residencia, uf, cidade, bairro, logradouro))
    elif tipo_reclamacao == '8':
        cursor.execute(
            'INSERT INTO troca_lampada (tipo_reclamacao, cpf, cep, numero_residencia, uf, cidade, bairro, logradouro) VALUES (?, ?, ?, ?, ?, ?, ?,?)',
            ('troca de lampada de iluminação publica',cpf_logado, cep, numero_residencia, uf, cidade, bairro, logradouro))

def obter_informacoes_cep():
    cep = input('Digite seu CEP: ')

    cep = cep.replace('-', '').replace(',', '').replace(' ', '')

    if len(cep) == 8:
        link = f'https://viacep.com.br/ws/{cep}/json/'

        requisicao = requests.get(link)

        if requisicao.status_code == 200:
            dic_requisicao = requisicao.json()

            uf = dic_requisicao.get('uf', '')
            cidade = dic_requisicao.get('localidade', '')
            bairro = dic_requisicao.get('bairro', '')
            logradouro = dic_requisicao.get('logradouro', '')

            return cep, uf, cidade, bairro, logradouro
        else:
            print('Não foi possível obter informações do CEP')
    else:
        print('CEP Inválido')
    return '', '', '', '', ''

def menu_reclamacoes():
    print()
    print()
    print("Escolha o tipo de reclamação:")
    print("1. Vazamento de Água")
    print("2. Esgoto a Céu Aberto")
    print("3. Buracos na Via")
    print("4. Furto de Energia")
    print("5. Fiação Elétrica Rompida")
    print("6. Lixo Acumulado")
    print("7. Poda de Árvores")
    print("8. Troca de Lâmpada de Iluminação Pública")
    print()
    print()
    tipo_reclamacao = input("Digite o número correspondente à reclamação: ")

    cep, uf, cidade, bairro, logradouro = obter_informacoes_cep()
    global cpf_logado
    numero_residencia = input("Digite o número da residência: ")
    return tipo_reclamacao,cpf_logado, cep, numero_residencia, uf, cidade, bairro, logradouro

print("Reclamação registrada com sucesso!")
