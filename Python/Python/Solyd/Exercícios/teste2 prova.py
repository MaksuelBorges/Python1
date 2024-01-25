import datetime
import tkinter as tk
from tkinter import ttk

class Bebida:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self):
        return f"Produto: {self.nome}, Quantidade: {self.quantidade}, Preço: R$ {self.preco:.2f}"

class Estoque:
    def __init__(self):
        self.produtos = []
        self.historico = []

    def adicionar_produto(self, produto, quantidade):
        for item in self.produtos:
            if item.nome == produto.nome:
                item.quantidade += quantidade
                self.registrar_movimentacao("Adição", produto, quantidade)
                return
        self.produtos.append(produto)
        self.registrar_movimentacao("Adição", produto, quantidade)

    def remover_produto(self, produto, quantidade):
        for item in self.produtos:
            if item.nome == produto.nome:
                if item.quantidade >= quantidade:
                    item.quantidade -= quantidade
                    self.registrar_movimentacao("Remoção", produto, quantidade)
                    return
                else:
                    return "Quantidade insuficiente no estoque."
        return "Produto não encontrado no estoque."

    def editar_produto(self, nome_antigo, novo_nome, novo_preco):
        for item in self.produtos:
            if item.nome == nome_antigo:
                item.nome = novo_nome
                item.preco = novo_preco
                self.registrar_movimentacao("Edição", item, 0, novo_nome, novo_preco)
                return
        return "Produto não encontrado no estoque."

    def mostrar_estoque(self):
        return [str(produto) for produto in self.produtos]

    def registrar_movimentacao(self, tipo, produto, quantidade, novo_nome=None, novo_preco=None):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if tipo == "Adição":
            self.historico.append(f"{timestamp}: Adicionado {quantidade} unidades de {produto.nome} ao estoque.")
        elif tipo == "Remoção":
            self.historico.append(f"{timestamp}: Removido {quantidade} unidades de {produto.nome} do estoque.")
        elif tipo == "Edição":
            self.historico.append(f"{timestamp}: Produto {produto.nome} editado para {novo_nome} (Preço: R$ {novo_preco:.2f}).")

estoque = Estoque()

def adicionar_produto():
    nome = nome_produto_entry.get()
    quantidade = int(quantidade_produto_entry.get())
    preco = float(preco_produto_entry.get())
    produto = Bebida(nome, quantidade, preco)
    estoque.adicionar_produto(produto, quantidade)
    update_estoque_list()

def remover_produto():
    nome = nome_produto_entry.get()
    quantidade = int(quantidade_produto_entry.get())
    produto = Bebida(nome, quantidade, 0)
    resultado = estoque.remover_produto(produto, quantidade)
    if resultado:
        resultado_label.config(text=resultado)
    else:
        resultado_label.config(text="Produto removido do estoque.")
    update_estoque_list()

def editar_produto():
    nome_antigo = nome_produto_entry.get()
    novo_nome = novo_nome_produto_entry.get()
    novo_preco = float(novo_preco_produto_entry.get())
    resultado = estoque.editar_produto(nome_antigo, novo_nome, novo_preco)
    if resultado:
        resultado_label.config(text=resultado)
    else:
        resultado_label.config(text="Produto editado no estoque.")
    update_estoque_list()

def update_estoque_list():
    estoque_list.delete(0, tk.END)
    for produto in estoque.mostrar_estoque():
        estoque_list.insert(tk.END, produto)

root = tk.Tk()
root.title("Distribuidora de Bebidas")

frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10)

nome_produto_label = ttk.Label(frame, text="Nome do Produto:")
nome_produto_label.grid(row=0, column=0, sticky="w")

nome_produto_entry = ttk.Entry(frame)
nome_produto_entry.grid(row=0, column=1, padx=5, pady=5)

quantidade_produto_label = ttk.Label(frame, text="Quantidade:")
quantidade_produto_label.grid(row=1, column=0, sticky="w")

quantidade_produto_entry = ttk.Entry(frame)
quantidade_produto_entry.grid(row=1, column=1, padx=5, pady=5)

preco_produto_label = ttk.Label(frame, text="Preço por Unidade (R$):")
preco_produto_label.grid(row=2, column=0, sticky="w")

preco_produto_entry = ttk.Entry(frame)
preco_produto_entry.grid(row=2, column=1, padx=5, pady=5)

adicionar_button = ttk.Button(frame, text="Adicionar Produto", command=adicionar_produto)
adicionar_button.grid(row=3, column=0, padx=5, pady=10)

remover_button = ttk.Button(frame, text="Remover Produto", command=remover_produto)
remover_button.grid(row=3, column=1, padx=5, pady=10)

editar_button = ttk.Button(frame, text="Editar Produto", command=editar_produto)
editar_button.grid(row=3, column=2, padx=5, pady=10)

novo_nome_produto_label = ttk.Label(frame, text="Novo Nome do Produto:")
novo_nome_produto_label.grid(row=4, column=0, sticky="w")

novo_nome_produto_entry = ttk.Entry(frame)
novo_nome_produto_entry.grid(row=4, column=1, padx=5, pady=5)

novo_preco_produto_label = ttk.Label(frame, text="Novo Preço por Unidade (R$):")
novo_preco_produto_label.grid(row=5, column=0, sticky="w")

novo_preco_produto_entry = ttk.Entry(frame)
novo_preco_produto_entry.grid(row=5, column=1, padx=5, pady=5)

resultado_label = ttk.Label(frame, text="", font=("Arial", 12, "bold"))
resultado_label.grid(row=6, column=0, columnspan=2, padx=5, pady=10)

estoque_list = tk.Listbox(frame, selectmode="single")
estoque_list.grid(row=7, column=0, columnspan=2, padx=5, pady=0)