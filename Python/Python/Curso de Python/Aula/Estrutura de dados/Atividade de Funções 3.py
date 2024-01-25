'''
#1. Escreva uma função que recebe uma lista de números e retorna uma nova lista com
#o dobro dos elementos

def dobro_elementos(lista):
    return list(map(lambda x: x * 2, lista))
lista_int = [1,2,3,4,5,6,7,8,9,10,20,30,40]
print(lista_int)
print(dobro_elementos(lista_int))
''' #1. Lista que retorna com o dobro.

'''
#2. Escreva uma função que recebe uma lista de strings e retorna uma nova lista com
#as strings invertidas.

def inverter_string(lista):
    return list(map(lambda s: s[1:] + s[0], lista))
lista_str = ['Maksuel', 'Camila', 'Maria', 'Pedro', 'Goku']
print(inverter_string(lista_str))
''' #2. Retorna uma lista invertida.

'''
#3. Escreva uma função que recebe uma lista de números e retorna uma nova lista com
#os números quadrados.
def quadrado(lista):
    return list(map(lambda x: x ** 2, lista))
quadrado_lista = [1,2,3,4,5,6,7,8,9,10,20,30]
print(quadrado_lista)
print(quadrado(quadrado_lista))
''' #3 Retorna uma lista com quadrado.

'''
#4. Escreva uma função que recebe uma lista de números e retorna uma nova lista com
#os números pares.

def pares(lista):
    return list(filter(lambda x: x % 2 == 0, lista))
pares_lista = [1,2,3,4,5,6,7,8,9,10,20,30,40]
print(pares_lista)
print(pares(pares_lista))
''' #4 Retora se é par

'''
#5. Escreva uma função que recebe uma lista de strings e retorna uma nova lista com
#as strings que começam com uma letra maiúscula.

def maiuscula(lista):
    return list(filter(lambda s: s[0].isupper(), lista))
maiuscula_lista = ['maksuel', 'Ana', 'pedro', 'Peppa','CASCAO']
print(maiuscula_lista)
print(maiuscula(maiuscula_lista))
''' #5 String começa com a letra maiuscula.

'''
#6. Escreva uma função que recebe uma lista de números e retorna uma nova lista com
#os números maiores que 10.

def maiores_dez(lista):
    return list(filter(lambda x: x>10, lista))
maior_lista = [5,6,7,8,9,10,20,30,33,777,2,78]
print(maior_lista)
print(maiores_dez(maior_lista))
''' #6 Imprimir numeros acima de 10.

'''
#7. Escreva uma função que recebe uma lista de números e retorna a soma dos
#elementos.
#Importa biblioteca
from functools import reduce
def soma_elementos(lista):
    return reduce(lambda x,y: x+y, lista)
print(lista)
soma_lista = [1,2,3,4,5,6,7,8,9,10,11,20,30]

print(soma_elementos(soma_lista))
''' #7 Retorna a soma dos elementos

'''
#8. Escreva uma função que recebe uma lista de números e retorna a média dos
#elementos.

def media_lementos(lista):
    media = sum(lista) / len(lista)
    return media
media_lista = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(maior_lista)
print(media_lementos(media_lista))
''' #8 Retorna a media da lista.

'''
#9. Escreva uma função que recebe uma lista de números e retorna o maior elemento.
from functools import reduce
def maior_elemento(lista):
    return reduce(lambda x, y: x if x> y else y, lista) # Pode-se substituir por max()
maior_lista = [1,2,3,4,6,7,8,9,1,22,99,136,795,12]
print(maior_lista)
print(maior_elemento(maior_lista))
''' #9 Retorna o maior numero da lista.

'''
#10 Escreva uma função que recebe uma lista de strings e retorna a string concatenada
from functools import reduce
def concatenar_string(lista):
    return reduce(lambda x, y: x + y, lista)
lista_string = ['AZUL', 'MAKSUEL', 'MARIA', 'GABI', 'ANA']
print(lista_string)
print(concatenar_string(lista_string))
''' #10 Retornar uma string concatenada.

'''
#1. Escreva uma função que recebe uma lista de números e retorna uma lista com os
#números primos.

def numeros_primos(lista):
    def eh_primo(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return list(filter(eh_primo, lista))
lista_numeros = [1,8,9,15,13,61,4555,48,178,852,63,189,452,654,798,185,163]
print(lista_numeros)
print(numeros_primos(lista_numeros))

''' #11 Numeros primos.

'''
#12. Escreva uma função que recebe uma lista de strings e retorna uma lista com as
#strings que são palíndromas.

def palindromes(lista):
    palindromes = []
    for string in palindromes_lista:
        if string == string[::-1]:
            palindromes.append(string)
    return palindromes
palindromes_lista = ['maksuel', 'socos', 'sós', 'salas','faca', 'listas', 'armario','rir']
print(palindromes_lista)
print(palindromes(palindromes_lista))
''' #12 Polindromas.

'''
#13 Escreva uma função que recebe uma lista de números e retorna uma lista com os
#números de Fibonacci.

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    lista_fibonacci = [0, 1]
    while len(lista_fibonacci) < n:
        proximo_numero = lista_fibonacci[-1] + lista_fibonacci[-2]
        lista_fibonacci.append(proximo_numero)
    return lista_fibonacci

n = 20  # Quantidade de números de Fibonacci desejados
resultado = fibonacci(n)
print(f'Numeros fibonacci: ', resultado)
''' #13 Fibonacci.