#Crie um módulo chamado `lista_util` com uma função que retorna o maior elemento de uma lista.

def maior_elemento(lista):
    if not lista:
        return None  # Retorna None se a lista estiver vazia
    return max(lista)