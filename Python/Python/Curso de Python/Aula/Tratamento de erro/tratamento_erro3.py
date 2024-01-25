#3 Crie uma função que receba uma lista e um índice, e retorne o elemento naquele índice.
#Trate o erro se o índice estiver fora dos limites da lista.

def acessar_elementos(lista, indice):
    try:
        elemento = lista[indice]
        return elemento
    except IndexError:
        return 'Erro: Indice fora dos limites da lista.'

#exemplo
print(acessar_elementos([1,2,3,4,5,6,], 3))