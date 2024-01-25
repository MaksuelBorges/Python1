import datetime

# Lista para armazenar os itens
itens = []

# Função para exibir o menu
def exibir_menu():
    print("\nMenu:")
    print("1. Incluir um item na lista")
    print("2. Alterar/atualizar um item na lista")
    print("3. Buscar um itompra de um item")
    print("6. Manipular e gravar inem na lista")
    print("4. Excluir um item da lista")
    print("5. Mostrar a hora da cformações em um arquivo")
    print("7. Sair")

# Função para incluir um item na lista
def incluir_item():
    item = input("Digite o item a ser incluído na lista: ")
    itens.append((item, datetime.datetime.now()))
    print("Item incluído na lista.")

# Função para alterar um item na lista
def alterar_item():
    if not itens:
        print("A lista está vazia. Nada para atualizar.")
    else:
        for i, (item, hora_compra) in enumerate(itens, 1):
            print(f"{i}. {item} (Hora da compra: {hora_compra.strftime('%Y-%m-%d %H:%M:%S')})")
        numero = int(input("Digite o número do item a ser atualizado: "))
        if 1 <= numero <= len(itens):
            novo_item = input("Digite o novo valor do item: ")
            itens[numero - 1] = (novo_item, itens[numero - 1][1])
            print("Item atualizado na lista.")
        else:
            print("Número de item inválido. Tente novamente.")

# Função para buscar um item na lista
def buscar_item():
    termo_busca = input("Digite o termo que deseja buscar: ")
    resultados = [(item, hora_compra) for item, hora_compra in itens if termo_busca in item]
    if resultados:
        print("Resultados encontrados:")
        for i, (item, hora_compra) in enumerate(resultados, 1):
            print(f"{i}. {item} (Hora da compra: {hora_compra.strftime('%Y-%m-%d %H:%M:%S')})")
    else:
        print("Nenhum resultado encontrado.")

# Função para excluir um item da lista
def excluir_item():
    if not itens:
        print("A lista está vazia. Nada para excluir.")
    else:
        for i, (item, hora_compra) in enumerate(itens, 1):
            print(f"{i}. {item} (Hora da compra: {hora_compra.strftime('%Y-%m-%d %H:%M:%S')})")
        numero = int(input("Digite o número do item a ser excluído: "))
        if 1 <= numero <= len(itens):
            del itens[numero - 1]
            print("Item excluído da lista.")
        else:
            print("Número de item inválido. Tente novamente.")

# Função para manipular e gravar informações em um arquivo
def gravar_em_arquivo():
    nome_arquivo = input("Digite o nome do arquivo para gravar informações: ")
    with open(nome_arquivo, 'w') as arquivo:
        for item, hora_compra in itens:
            arquivo.write(f"{item} (Hora da compra: {hora_compra.strftime('%Y-%m-%d %H:%M:%S')})\n")
    print(f"As informações foram gravadas no arquivo '{nome_arquivo}'.")

# Loop principal
while True:
    exibir_menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        incluir_item()

    elif escolha == "2":
        alterar_item()

    elif escolha == "3":
        buscar_item()

    elif escolha == "4":
        excluir_item()

    elif escolha == "5":
        alterar_item()

    elif escolha == "6":
        gravar_em_arquivo()

    elif escolha == "7":
        print("Saindo do programa. Obrigado!")
        break

    else:
        print("Opção inválida. Tente novamente.")