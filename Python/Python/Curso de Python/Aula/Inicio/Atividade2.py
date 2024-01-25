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

#Tabela de códigos dos itens acima, tambem variaveis.
tabela_codigo = {
    1: 0.50,
    2: 1.00,
    3: 4.00,
    5: 7.00,
    9: 8.00
}

total = 0
#Bloco de repetição
while True:
    try:
        #Entrada do teclado
        codigo = input('Digite o código do produto: ')
        #Adicionando um parada S ou s
        if codigo == 'S' or codigo == 's':
            break
        if codigo != 'S' or codigo != 's':
            codigo = int(codigo)
        quantidade = int(input('Digite a quantidade: '))
        if codigo in tabela_codigo:
            valor_codigo = tabela_codigo[codigo]
            itens = valor_codigo * quantidade
            valor = valor + itens
            print(f'Código do produto: {valor_codigo}',f'\nQuantidade: {itens}',f'Valor da compra: {valor}')
        #Se o código não existe
        else:
            print ('Código inválido!')
    except ValueError:
        print('Valor invalido')
print(f'Total: {valor:.2f}')
