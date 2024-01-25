#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

aluno = input('Qual o nome do aluno: ')
nota1 = float(input('Qual a nota obtida na primeira avaliação: '))
nota2 = float(input('Qaul a nota obtida na segunda avaliação: '))
v1 = (nota1+nota2)/2

print(f'A media do {aluno} dessa matéria é {v1:.2f}')

