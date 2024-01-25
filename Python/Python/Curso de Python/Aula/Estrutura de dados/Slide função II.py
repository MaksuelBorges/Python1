'''
1. Escreva uma função recursiva que calcula o fatorial de um número.

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
num = int(input('Informe um numero: '))
print(fatorial(num))
''' # Fatorial

'''
#Escreva uma função recursiva que calcula o número de Fibonacci de um número.

dobro = lambda x: x * 2
print(dobro(5))
''' #Calcula o numero de fabonacci

'''
#3. Escreva uma função recursiva que imprime os números de 1 a n.

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
numero = int(input('informe um numero para saber se é Fibonacci: '))
print(f'O numero {numero} na sequencia de Fibonacci é {fibonacci(numero)}')
''' #Regressiva

'''
def imprimir_numeros(n):
    if n > 0:
        imprimir_numeros(n - 1)
        print(n)
numero = int(input('Informe um numero: '))
imprimir_numeros(numero)
''' #Imprimir numeros em sequencia

'''
#4. Escreva uma função recursiva que inverte uma string

def inverter_string(s):
    if len(s) == 0:
        return s
    else:
        return inverter_string(s[1:]) + s[0]
palavra = input('Informe uma palavra: ')
print(f'A palavra {palavra} foi invertida para {inverter_string(palavra)}')
''' #Inverter string

'''
#5. Escreva uma função recursiva que encontra o máximo de uma lista de números

def encontrar_maximo(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        max_sublista = encontrar_maximo(lista[1:])
        return lista[0] if lista[0] > max_sublista else max_sublista
lista = [100, 500, 1000, 8425, 8977, 8877]
print(encontrar_maximo(lista))
''' #Econtra o maximo

'''
#6 Escreva uma função recursiva que encontra o mínimo de uma lista de números

def encontrar_minimo(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        min_sublista = encontrar_minimo(lista[1:])
        return lista[0] if lista[0] < min_sublista else min_sublista
lista = [111,5855,110,111,123,517,1,22222,955]
print(lista)
print(min(lista)) # Da mesma forma que a função para encontrar o minimo  da lista
print(max(lista)) # Da mesma forma que a função para encontar o maximo da lista
print(encontrar_minimo(lista)) # Imprime a função
''' #Encontre o minimo

'''
#7. Escreva uma função recursiva que soma os elementos de uma lista de números

def soma_lista(lista):
    if len(lista) == 1:
        return [0]
    else:
        return lista[0] + soma_lista(lista[1:])
lista = [111, 32,585,7899,4125,6325,4122]
print(soma_lista(lista))
''' #Soma os elementos da lista

'''
#13. Escreva uma função lambda que retorna o número de caracteres de uma string.
contar_caracteres = lambda s: len(s)
print(contar_caracteres('Maksuel'))
''' #Soma caracteres

'''
#Escreva uma função lambda que retorna True se um número é par, ou False se um
número é ímpar.
par = lambda x: x % 2 == 0
print(par(44))
''' #True para 'par'.

'''
#16. Escreva uma função lambda que retorna a média dos elementos de uma lista de
#números
soma_lista_lambda = lambda lista: sum(lista)
lista = [200,212,22,321]
print(soma_lista_lambda(lista)) #Puxa a variavel com o parametro
print(sum(lista))
''' #Media lista de numeros
