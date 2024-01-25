''' #Math
#Exercício 1: Calcule a raiz quadrada de um número usando o módulo `math`.

import math
print(math.sqrt(25)) #math modulo de matematica sqrt raiz quadrada
'''

''' #Random numero telefone
#Exercício 5: Crie uma função que gere um número aleatório de telefone formatado usando o módulo `random`.
import random
def gerar_numero_de_telefone():
    numero = ''.join([str(random.randint(0,9)) for _ in range(10)])
    numero_formatado = f'({numero[0:3]}) 98 {numero[0:10:4]}-{numero[0:10:3]}'
    return numero_formatado
telefone = gerar_numero_de_telefone()
print(f'Numero de telefone: {telefone}')
'''

'''#OS
#Exercício 3: Crie uma função que liste todos os arquivos em um diretório usando o módulo `os`.

import os

diretorio = C:/SER/maksu/Documents/Python/Módulos II'
arquivos = os.listdir(diretorio)
print ('Arquivos no diretório.')
print(arquivos)
'''

''' #JSON
#Exercício 4: Converta um dicionário para uma string JSON usando o módulo `json`.

import json
dicionario = {'nome': 'Maksuel', 'idade': 90}
string_json = json.dumps(dicionario)
print('Dicionario em JSON: ')
print(string_json)
'''

''' #Numero 1-100 random

#Exercício 2: Gere um número aleatório entre 1 e 100 usando o módulo `random`.

import random
print(random.randint(1,100))
'''

''' #Angulo modulo math

#Exercício 6: Calcule o cosseno de um ângulo usando o módulo `math`

import math

angulo = 60

angulo_radiano = math.radians(angulo)
cosseno = math.cos(angulo_radiano)
print(f'O cosseno de 60º é: {cosseno}')
'''

''' #Modulo litando outros diretorios
#Exercício 7: Crie uma função que liste todos os diretórios em um diretório usando o módulo `os`.
import os
diretorios = [nome for nome in os.listdir(diretorio)]
'''

'''#10 numeros aleatorios
#Exercício 8: Gere uma lista de 10 números inteiros aleatórios entre 1 e 100 usando o módulo `random`.
import random

numeros_inteiros = [random.randint(1, 100) for _ in range(10)]
print(f'Lista de numeros inteiros aleatorios: ')
print(numeros_inteiros)
'''

# se é numero primo com math
'''
#Exercício 9: Crie uma função que verifique se um número é primo usando o módulo `math`.
import math
def numeros_primos(numero):
    if numero <= 1:
        return False
    for i in range(2, int(math.sqrt(numero))+ 1):
        if numero % 1 == 0:
            return False
    return True 
numero1 = [1,8,9,15,13,61,4555,48,178,852,63,189,452,654,798,185,163]
if numeros_primos(numero1):
    print(f'{numero1}, é um numero primo.')
else:
    print(f'{numero1}, não é um numero primo.')

'''
'''
#Exercício 10: Gere uma lista de 5 números float aleatórios entre 0 e 1 usando o módulo `random`.

import random

numeros_float = [random.uniform(0, 1) for _ in range(5)]

print('Lista de numeros float aleatorios: ')
print(numeros_float)
'''