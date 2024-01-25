'''
#Imprimir Números Pares: Escreva um programa que use um loop for para
#imprimir todos os números pares de 2 a 20

for numero in range(2,21): # ou de forma mais pratica (2,21,2):
    if (numero % 2) == 0:
        print(numero)
'''
'''
Calcular a Média de Notas: Crie um programa que use um loop for para calcular a 
média de notas em uma lista de notas dadas como entrada.

notas= [2,4,5,6]
for nota in(notas):
    total = sum(notas)
    media_notas = total / len(notas)
print(f'A média do aluno é: {media_notas}')
'''
'''
Tabuada de Multiplicação: Escreva um programa que solicita um número ao
usuário e, em seguida, use um loop for para imprimir a tabuada de multiplicação
desse número, de 1 a 10.
'''
numero = int(input('Digite o numero para calcular a tabuada:'))
for contador in range(1,11):
    tabuada = numero * contador
    print(f'{numero}x{contador}= {tabuada}')