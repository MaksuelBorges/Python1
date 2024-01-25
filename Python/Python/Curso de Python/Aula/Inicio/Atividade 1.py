#Calculadora prova

def somar(x, y):
    return x + y
def subtrair(x, y):
    return x - y
def multiplicar(x, y):
    return x * y
def dividir(x, y):
    if y == 0:
        return 'Erro: divisão por zero'
    return x / y

resultado = 0

while True:
    print(f'###### Menu ######')
    print(f' (+) Somar')
    print(f' (-) Subtrair')
    print(f' (*) Multiplicar')
    print(f' (/) Dividir')
    print(f' (0) Zerar resultado')
    print(f' (S) Sair')

    opcao = input('Escolha uma operação: ')

    if opcao == 'S' or opcao == 's':
        break
    elif opcao in ('+', '-', '*', '/'):
        num = float(input('Digite um numero: '))
        if opcao == '+':
            resultado = somar(resultado,num)
        elif opcao == '-':
            resultado = subtrair(resultado,num)
        elif opcao == '*':
            resultado = resultado*num
        elif opcao == '/':
            resultado = dividir(resultado, num)
        print(f'Resultado atual: {resultado}')
    elif opcao == '0':
        resultado = 0
        print('Resultado zerado')
    else:
        print('Opção invalida!')
print('Calculadora encerrada.')