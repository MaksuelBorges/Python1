#Crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar.

n = int(input('Par ou impar: '))
if n%2 == 0:
    print(f'{n} é PAR!')
else:
    print(f'{n} é IMPAR')