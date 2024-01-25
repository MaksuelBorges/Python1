'''
#1. Atividade 1: Crie um array NumPy contendo os números pares de 2 a 10 e, em seguida,
#calcule a média desses números.

import numpy as np

#criando um array numpy com numeros pares de 2 a 10

arr = np.array([2,4,6,8,10])
#calcule a media dos numeros no array
media = np.mean(arr)

print(f'array numpy: {arr}')
print(f'Media dos numeros: {media}')
''' #1. NumPy array numero par 2-10

'''
#2. Atividade 2: Crie dois arrays NumPy com números inteiros e realize operações de adição,
#subtração, multiplicação e divisão elementar entre eles.

import numpy as np
#A quantidade dos elementos tem que ser iguais a de outro vetor para fazer o calculo
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([2,4,6,8,10])

soma = arr1 + arr2
subtracao = arr1 - arr2
multiplicacao = arr1 * arr2
divisao = arr1 / arr2
print(f'Soma: {soma}')
print(f'Subtração: {subtracao}')
print(f'Multiplicação: {multiplicacao}')
print(f'Divisão: {divisao}')
''' #2. Numpy calculo basico

'''
#1. Atividade 1: Crie um DataFrame com informações de nomes, idades e cidades de
#algumas pessoas e, em seguida, calcule a média das idades.

import pandas as pd

dados = {'Nome': ['Maksuel', 'Jessica', 'Xuxa'], 'Idade': [22,32,39], 'Cidade': ['Cuiaba','São paulo', 'Argentina']}

df = pd.DataFrame(dados)
media_idade = df['Idade'].mean()

print('DataFreme: ')
print(df)
print(f'Média das idades: {media_idade}')
''' #3. Pandas DataFrame

'''
#2. Atividade 2: Crie um DataFrame com dados fictícios de vendas, incluindo produtos,
#quantidades e preços. Calcule o total de vendas para cada produto.

import pandas as pd

dados = {'Produtos': ['Carne', 'Refrigerante','Cerveja', 'Bolo'], 'Quantidade': [5,12,24,2], 'Preços': [48,3,5,58]}
df = pd.DataFrame(dados)
df['Total a Pagar'] = df['Quantidade'] * df['Preços']
resultado = df['Total a Pagar'].sum()
print('DataFreme: ')
print(df)
print('Total a Pagar R$',resultado)
''' #4. Pandas DataFreme Vendas

'''
#Atividade 1: Crie um gráfico de barras simples representando a contagem de votos para
#diferentes candidatos em uma eleição fictícia.

import matplotlib.pyplot as plt

candidato = ['Maksuel', 'Pedro', 'Henrique', 'Carlos']
voto = [10000,22000,50000,7842]

# Crie um grafico de barras
plt.bar(candidato, voto)
plt.xlabel('Candidato')
plt.ylabel('Numeros de votos')
plt.title('Resultado da eleição')
plt.show()
''' #5. Matplotlib fazer grafico

'''
#2. Atividade 2: Crie um gráfico de linha que mostre a evolução do preço de uma ação ao longo do tempo.

import matplotlib.pyplot

meses = ['janeiro', 'fevereiro', 'março', 'abriu', 'maio']
preco = [9000,1200,5000,18000,15000]

matplotlib.pyplot.plot(meses, preco)
matplotlib.pyplot.show()
''' #6. Matplotlib grafico com progeção de valor em linha

#Atividade 1: Escreva um programa que faça uma solicitação HTTP a uma URL e exiba o status da resposta (código de status) na tela.

import requests
url = 'https://www.google.com'
print('Codigo', )