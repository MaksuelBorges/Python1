import sqlite3
from modulo_login import fazer_login, cadastrar_usuario, alterar_informacoes_pessoais
from modulo_reclamacoes import inserir_reclamacao, menu_reclamacoes
from listar_reclamacoes import listar_reclamacoes_usuario


conexao = sqlite3.connect('SAI.db')
cursor = conexao.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    cpf INTEGER PRIMARY KEY,
                    nome TEXT(100),
                    senha TEXT,
                    nascimento TEXT(10),
                    email TEXT(100),
                    celular INTEGER(13)
                )''')

def main():
    while True:
        print("\n  ==========================================")
        print("  ==||                                  ||==")
        print("  ==||                                  ||==")
        print("  ==||SISTEMA DE ATENDIMENTO INTELIGENTE||==")
        print("  ==||                                  ||==")
        print("  ==||                                  ||==")
        print("  ==========================================")

        escolha = input("\t\t1-  FAZER LOGIN\n\n"                    
                        "\t\t2 - CRIAR NOVO USUARIO\n")
        if escolha in ['1', '2']:
            try:
                if escolha == '1':
                    fazer_login()
                    print(f'{cpf_logado}')
                    menu_usuario()


                elif escolha == '2':
                    cpf_cadastrado = cadastrar_usuario()
                    cpf = cpf_cadastrado
                    menu_usuario()

                else:
                    print("Opção inválida. Tente novamente.")

            except Exception as e:
                print("Ocorreu um erro:", e)
def menu_usuario():
    while True:
        print("MENU DO USUÁRIO")
        print("1. Inserir reclamação")
        print("2. Listar reclamações")
        print("3. Alterar informações pessoais")
        print("4. Fazer logoff")
        opcao = input("Escolha uma opção (1/2/3/4): ")
        global cpf_logado
        if opcao == "1":
            tipo_reclamacao,cpf_logado, cep, numero_residencia, uf, cidade, bairro, logradouro = menu_reclamacoes()
            inserir_reclamacao(tipo_reclamacao, cpf_logado, cep, numero_residencia, uf, cidade, bairro, logradouro)
            print("Reclamação registrada com sucesso!")

        elif opcao == "2":
            reclamacoes_usuario = listar_reclamacoes_usuario(cpf_logado)
            if reclamacoes_usuario:
                print("Reclamações do usuário:")
                for reclamacao in reclamacoes_usuario:
                    print(reclamacao)
            else:
                print("Nenhuma reclamação encontrada para este usuário.")


        elif opcao == "3":

            alterar_informacoes_pessoais(cpf_logado)


        elif opcao == "4":
            print("Fazendo logoff...")
            fazer_login()
            break

        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()