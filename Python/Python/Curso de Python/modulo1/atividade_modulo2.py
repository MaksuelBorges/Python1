''' #Math
#Exercício 1: Calcule a raiz quadrada de um número usando o módulo `math`.

import math
print(math.sqrt(25)) #math modulo de matematica sqrt raiz quadrada
''' #Math

''' 
#Exercício 5: Crie uma função que gere um número aleatório de telefone formatado usando o módulo `random`.
import random
def gerar_numero_de_telefone():
    numero = ''.join([str(random.randint(0,9)) for _ in range(10)])
    numero_formatado = f'({numero[0:3]}) 98 {numero[0:10:4]}-{numero[0:10:3]}'
    return numero_formatado
telefone = gerar_numero_de_telefone()
print(f'Numero de telefone: {telefone}')
''' #Random numero telefone

'''
#Exercício 3: Crie uma função que liste todos os arquivos em um diretório usando o módulo `os`.
import os

diretorio = 'C:/Users/maksu/PycharmProjects/MaksuelBorges1/venv/urso de Python/Módulos I>'
diretorios = [nome for nome in os.listdir(diretorio) if os.path.isdir(os.join(diretorio, name))]
print ('Arquivos no diretório.')
for diretorio in diretorios:
    print(f'Diretorio: {diretorio}')

''' #Diretorio e arquivos

'''
#Exercício 4: Converta um dicionário para uma string JSON usando o módulo `json`.

import json
dicionario = {'nome': 'Maksuel', 'idade': 90}
string_json = json.dumps(dicionario)
print('Dicionario em JSON: ')
print(string_json)
''' #JSON

'''

#Exercício 2: Gere um número aleatório entre 1 e 100 usando o módulo `random`.

import random
print(random.randint(1,100))
''' #Numero 1-100 random

'''
#Exercício 6: Calcule o cosseno de um ângulo usando o módulo `math`

import math

angulo = 60

angulo_radiano = math.radians(angulo)
cosseno = math.cos(angulo_radiano)
print(f'O cosseno de 60º é: {cosseno}')
''' #Calcule o cosseno de um ângulo usando o módulo `math`

'''
#7 Crie uma função que liste todos os diretórios em um diretório usando o módulo `os`.

import os
diretorio = 'C:/Users/maksu/PycharmProjects/MaksuelBorges1/venv/Curso de Python/Módulos I'
diretorios = [nome for nome in os.listdir(diretorio) if os.path.isdir(os.path.join(diretorio, nome))]
print('Diretorio no diretorio: ')
for diretorio in diretorios:
    print(f'Diretorios: {diretorio}')
''' #Diretorio no diretorio

'''''
#Gere uma lista de 10 números inteiros aleatórios entre 1 e 100 usando o módulo `random`.

import random

numeros_aleatorios = random.sample(range(1,101), 10)
print(numeros_aleatorios)
''''' #10 random de 1-100

'''
#Crie uma função que verifique se um número é primo usando o módulo `math`

import math

def numeros_primos(lista):
    def eh_primo(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    return list(filter(eh_primo, lista))
lista_numeros = [1,8,9,15,13,61,4555,48,178,852,63,189,452,654,798,185,163]
print(lista_numeros)
print(numeros_primos(lista_numeros))
'''#11 Math primo

'''
#Gere uma lista de 5 números float aleatórios entre 0 e 1 usando o módulo `random`.
import random

numeros_float = [random.uniform(0, 1) for f in range(5)]
print('Lista de numeros float aleatorios: ')
print(numeros_float)
'''#12 float entre 0-1