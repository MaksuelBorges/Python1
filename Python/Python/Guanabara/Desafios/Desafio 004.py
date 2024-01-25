#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas
#as informações possiveis sobre ela
#LEMBRANDO: INPUT SMP SERÁ STR!!! ainda não sei como alterar o tipo.. você entendeu.
objeto = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(objeto)}')
print(f'Só tem espaços? {objeto.isspace()}')
print(f'É um número? {objeto.isnumeric()}')
print(f'É alfabético? {objeto.isalpha()}')
print(f'É alfanumérico? {objeto.isalnum()}')
print(f'Está em maiúsculas? {objeto.isupper()}')
print(f'Está em minúsculas? {objeto.islower()}')
print(f'Está capitalizado? {objeto.istitle()}')
