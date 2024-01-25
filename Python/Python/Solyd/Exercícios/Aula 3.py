#Faça um programa que pergunte a idade, o peso e a altura de uma pessoa
#e decide se ela está apta a ser do exercito. Para entrar no exercito é preciso
#ter mais de 18 anos pesar mais ou igual 60kg e medir mais que 1,70m

idade = int(input('Qual sua idade? '))
peso = float(input('Quanto pesa? '))
altura = float(input('Qual sua altura? '))

if idade >= 18 and peso >= 60 and altura >= 1.70:
    print('Você está apto a servir o exercito!!!')
else:
    print('Você não está apto há server o exercito!!!')