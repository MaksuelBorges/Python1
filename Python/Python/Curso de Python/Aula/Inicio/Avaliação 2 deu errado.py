#Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código
#do produto e a quantidade comprada. Utilize a tabela de códigos a seguir para obter o preço de cada produto.

print('====== Registradora do Maks ======')
print('======== Meu de opções ===========')
print('[1] - Balas         --> R$0,50')
print('[2] - Paçoca        --> R$1,00')
print('[3] - Bis Oreo      --> R$4,00')
print('[5] - Sprite 2L     -->R$7,00')
print('[9] - Coca-cola 2L  -->R$8,00')
print('[S] - Finalizar compra')
#Váriaveis
c1 = 1
c2 = 2
c3 = 3
c4 = 5
c5 = 9
codigo1 = int(input('Digite o código do produto: '))
codigo2 = float(input('Digita a quantidade: \t'))
if codigo1 == 1:
    total = 0.50 * codigo2
elif codigo1 == 2:
    total = 1 * codigo2
elif codigo1 == 3:
    total = 4.00 * codigo2
elif codigo1 == 5:
    total = 7.00 * codigo2
elif codigo1 == 6:
    total = 8.00 * codigo2
else:
    total = 7 or 6 or 4 or 8
    print ('Codigo invalido')
print(f'Total: {total}')