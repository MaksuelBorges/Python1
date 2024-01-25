import sqlite3

conexao = sqlite3.connect('SAI.db')
cursor = conexao.cursor()

def cadastrar_usuario():
    print("Crie um novo usuário e senha para acessar o programa.")
    while True:
        cpf = int(input("Digite o CPF: "))
        nome = input("Digite um nome de usuário: ")
        senha = input("Digite uma senha: ")
        nascimento = input("Digite sua data de nascimento: ")
        email = input("Digite seu email: ")
        celular = int(input("Digite seu celular: "))

        cursor.execute("SELECT cpf FROM usuarios WHERE cpf=?", (cpf,))
        resultado = cursor.fetchone()

        if resultado:
            print("CPF já existe. Por favor, insira outro CPF.")
        else:
            cursor.execute('''INSERT INTO usuarios (cpf, nome, senha, nascimento, email, celular)
                            VALUES (?, ?, ?, ?, ?, ?)''',
                           (cpf, nome, senha, nascimento, email, celular))
            conexao.commit()
            print("Usuário cadastrado com sucesso!")
            fazer_login()
            return cpf

cpf_logado = None

def fazer_login():
    global cpf_logado
    print("Faça seu login")
    cpf = int(input("Digite o CPF: "))
    senha = input("Digite a senha: ")

    cursor.execute("SELECT cpf FROM usuarios WHERE cpf = ? AND senha = ?", (cpf, senha))
    resultado = cursor.fetchone()

    if resultado:
        cpf_logado = resultado[0]
        print("Login bem-sucedido!")
        return cpf_logado
    else:
        print("CPF não existe ou senha incorreta.")
        return None

def alterar_informacoes_pessoais(cpf_logado):
    print("ALTERAR INFORMAÇÕES PESSOAIS")
    novo_nome = input("Digite o novo nome de usuário: ")
    nova_senha = input("Digite a nova senha: ")
    novo_email = input("Digite o novo email: ")
    novo_celular = int(input("Digite o novo número de celular: "))

    conexao = sqlite3.connect('SAI.db')
    cursor = conexao.cursor()

    # Atualiza as informações na tabela de usuários
    cursor.execute('''
        UPDATE usuarios
        SET nome=?, senha=?, email=?, celular=?
        WHERE cpf=?
    ''', (novo_nome, nova_senha, novo_email, novo_celular, cpf_logado))

    conexao.commit()
    conexao.close()

    print("Informações pessoais atualizadas com sucesso!")