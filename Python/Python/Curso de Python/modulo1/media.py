#Crie um módulo chamado `media` com funções para calcular a média aritmética e a média
#ponderada de uma lista de números.
def media_aritmetica(lista): #Media aritmetica
    if not lista:
        return 0
    return sum(lista) / len(lista)

def media_ponderada(lista, pesos): #media ponderada
    if not lista or not pesos or len(lista) != len(pesos):
        return 0
    total_pontos = sum([valor * peso for valor, peso in zip(lista, pesos)])
    total_pesos = sum(pesos)
    return total_pontos / total_pesos