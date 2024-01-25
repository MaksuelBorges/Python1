
#1 Crie um arquivo chamado "texto.txt" e escreva nele uma mensagem de sua escolha.

arquivo = open('texto.txt', 'w')
arquivo.write('PROVA SEMANA QUE VEM DIA 8 9 E 10.')
arquivo.close()

#2 Leia o conteúdo do arquivo "texto.txt" e imprima na tela.
arquivo = open('texto.txt', 'r')
conteudo = arquivo.read()
print(conteudo)
arquivo.close() # fecha o arquivo

#3 Crie uma lista de strings e escreva cada elemento em uma linha do arquivo "lista.txt".
lista_de_strings = ['Prova no dia 7 quarta-feira', 'Prova tambem no dia 8 quinta-feira', 'Por fim prova dia 9 sexta-feira']
with open('lista.txt', 'w') as arquivo:
    for item in lista_de_strings:
        arquivo.write(item + '\n')

#4 Leia o conteúdo do arquivo "lista.txt" e armazene cada linha em uma lista.
with open('lista.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    lista = [linha.strip() for linha in linhas]
    print(lista)

#5 Crie uma função que receba um nome de arquivo e conte quantas palavras ele possui.
'''
#6 Crie um programa que renomeie o arquivo "texto.txt" para "novo_texto.txt".
import os
os.rename('texto.txt', 'novo_txt')
'''
'''
#7 Crie um novo diretório chamado "meus_arquivos" e mova o arquivo "novo_texto.txt" para esse diretório.
import shutil
os.makedirs('meus_arquivos')
shutil.move('novo_texto.txt')
'''