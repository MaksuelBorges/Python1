import sqlite3


def listar_reclamacoes_usuario(cpf):
    conn = sqlite3.connect('SAI.db')
    cursor = conn.cursor()

    # Consulta para obter as reclamações do usuário com base no CPF
    cursor.execute('''
        SELECT * FROM vazamento_agua WHERE CPF = ?
        UNION ALL
        SELECT * FROM esgoto_ceu_aberto WHERE CPF = ?
        UNION ALL
        SELECT * FROM buracos_via WHERE CPF = ?
            UNION ALL
        SELECT * FROM furto_energia WHERE CPF = ?
            UNION ALL
        SELECT * FROM fiacao_eletrica_rompida WHERE CPF = ?
            UNION ALL
        SELECT * FROM lixo_acumulado WHERE CPF = ?
            UNION ALL
        SELECT * FROM poda_arvores WHERE CPF = ?
            UNION ALL
        SELECT * FROM troca_lampada WHERE CPF = ?
            UNION ALL

        ''', (cpf, cpf, cpf, cpf, cpf, cpf, cpf, cpf))

    reclamacoes = cursor.fetchall()
    print(reclamacoes)

    conn.close()

    return reclamacoes