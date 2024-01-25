import datetime

# Dicionário com os itens disponíveis para compra
itens = {
    '1': {'nome': 'Refrigerante', 'preco': 10.0},
    '2': {'nome': 'Cerveja', 'preco': 5.0},
    '3': {'nome': 'Doce', 'preco': 8.0},
}

carrinho = {}  # Dicionário para armazenar os itens no carrinho
compras = []  # Lista para armazenar o histórico de compras

def exibir_menu():
    print("===== Menu de Compras =====")
    for codigo, item in itens.items():
        print(f"{codigo}: {item['nome']} - R${item['preco']:.2f}")
    if carrinho:
        print("U: Atualizar Carrinho")
        print("E: Excluir Item do Carrinho")
    if compras:
        print("R: Recuperar Compra")
    print("C: Concluir Compra")
    print("F: Finalizar Programa")
    print("===========================")

def adicionar_item_carrinho(codigo, quantidade):
    if codigo in itens:
        item = itens[codigo]
        if codigo in carrinho:
            carrinho[codigo]['quantidade'] += quantidade
        else:
            carrinho[codigo] = {'nome': item['nome'], 'preco': item['preco'], 'quantidade': quantidade}

def atualizar_carrinho():
    if not carrinho:
        print("O carrinho está vazio. Não há itens para atualizar.")
        return
    exibir_carrinho()
    codigo = input("Digite o código do item que deseja atualizar: ").upper()
    if codigo in carrinho:
        nova_quantidade = int(input("Digite a nova quantidade desejada: "))
        carrinho[codigo]['quantidade'] = nova_quantidade
    else:
        print("Código de item no carrinho inválido. Tente novamente.")

def excluir_item_carrinho():
    if not carrinho:
        print("O carrinho está vazio. Não há itens para excluir.")
        return
    exibir_carrinho()
    codigo = input("Digite o código do item que deseja excluir do carrinho: ").upper()
    if codigo in carrinho:
        del carrinho[codigo]
    else:
        print("Código de item no carrinho inválido. Tente novamente.")

def recuperar_compra():
    if not compras:
        print("Não há histórico de compras disponível.")
        return
    print("===== Histórico de Compras =====")
    for i, compra in enumerate(compras, start=1):
        print(f"Compra {i}")
    compra_numero = int(input("Digite o número da compra que deseja recuperar: "))
    if 1 <= compra_numero <= len(compras):
        print(f"Detalhes da Compra {compra_numero}:")
        exibir_carrinho(compras[compra_numero - 1])
    else:
        print("Número de compra inválido. Tente novamente.")

def exibir_carrinho(carrinho=None):
    if carrinho is None:
        carrinho = {}
    print("===== Carrinho de Compras =====")
    total = 0
    for codigo, item in carrinho.items():
        subtotal = item['preco'] * item['quantidade']
        total += subtotal
        print(f"{item['nome']} - R${item['preco']:.2f} x{item['quantidade']} = R${subtotal:.2f}")
    print(f"Total: R${total:.2f}")
    print("===============================")

while True:
    exibir_menu()
    escolha = input("Digite o código do item desejado (ou 'C' para concluir a compra, 'F' para finalizar o programa): ").upper()

    if escolha == 'C':
        if carrinho:
            exibir_carrinho(carrinho)
            compras.append(carrinho.copy())
            carrinho.clear()
            data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Compra finalizada em {data_hora}")
        else:
            print("O carrinho está vazio. Não é possível concluir a compra.")
    elif escolha == 'U':
        atualizar_carrinho()
    elif escolha == 'E':
        excluir_item_carrinho()
    elif escolha == 'R':
        recuperar_compra()
    elif escolha == 'F':
        break  # Finalizar o programa
    elif escolha in itens:
        quantidade = int(input("Digite a quantidade desejada: "))
        adicionar_item_carrinho(escolha, quantidade)
    else:
        print("Código de item inválido. Tente novamente.")