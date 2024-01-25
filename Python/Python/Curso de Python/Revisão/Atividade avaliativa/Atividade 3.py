'''1. Verifique se um número é igual a outro número.
2. Verifique se um número é maior que outro número.
3. Verifique se uma string é igual a outra string.
4. Verifique se um número é menor ou igual a outro número.
5. Verifique se duas strings são diferentes.
'''
x = 8
y = 3
z = 'diferente'
z2 = 'diferente 777'

igual = x == y
maior = x > y
menor = x < y
txt_igual = z == z2
maior_igual = x >= y
menor_igual = x <= y
txt_diferente = z != z2

print(f'Numero 8 e 3 São?', f'\n\tIguais: {igual}', f'\n\tMaior: {maior}', f'\n\tMenor: {menor}', f'\n\tTexto iguais: {txt_igual}', f'\n\tTexto diferentes: {txt_diferente}', f'\n\tMaior ou igual: {maior_igual}', f'\n\tMenor ou igual: {menor_igual}')