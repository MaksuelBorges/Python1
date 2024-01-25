'''
# Crie uma função chamada calculadora que recebe dois números e um operador como
#entrada. A função deve realizar a operação correspondente (adição, subtração, multiplicação
#ou divisão) com base no operador fornecido e retornar o resultado. Peça ao usuário para
#fornecer os números e o operador, chame a função e exiba o resultado.

def calculadora(num1, num2, operacao):
    if operacao == operacao:
        if operacao == '+':
            return num1 + num2
        elif operacao == '-':
            return num1 - num2
        elif operacao == '*':
            return num1 * num2
        elif operacao == '/':
            return num1 / num2
num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))
operacao = input('Digite o operador (+, -, *, /): ')
resultado = calculadora(num1, num2, operacao)
print(f'Resultado: {resultado}')
''' #Calculadora simples com função

''' 
#Crie uma função chamada converte_temperatura que converte uma temperatura de graus
#Celsius para Fahrenheit. A fórmula de conversão é: Fahrenheit = (Celsius * 9/5) + 32. Peça
#ao usuário para inserir a temperatura em graus Celsius e, em seguida, chame a função
#converte_temperatura para realizar a conversão e exibir o resultado em Fahrenheit.

def converter_temperatura(celsius):
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
celsius = float(input('Quantos graus celsius está fazendo ai em cuiaba:'))
fahrenheit = converter_temperatura(celsius)
print(f'Temperatura em Fahrenheit: {fahrenheit}')
''' #Converter temperatura em Fahrenheit

'''
#Crie uma função chamada calculadora_avancada que aceita três argumentos: dois
#números e uma operação avançada (por exemplo, potenciação ou raiz quadrada). A função
#deve realizar a operação especificada com os dois números e retornar o resultado. Além
#disso, permita ao usuário escolher entre as operações básicas (adição, subtração,
#multiplicação, divisão) ou as operações avançadas. Peça ao usuário para fornecer os
#números, a operação e a escolha entre operações básicas ou avançadas, e chame a função
#calculadora_avancada para calcular o resultado.
def calculadora_avancada(num1, num2, operacao):
    if operacao == operacao:
        if operacao == '+':
            return num1 + num2
        elif operacao == '-':
            return num1 - num2
        elif operacao == '*':
            return num1 * num2
        elif operacao == '/':
            return num1 / num2
        else:
            print('Operação invalida!')
def operacao_avancada(avancada):
    if avancada == avancada:
        if avancada == 'X':
            return num1 ** (1 / num2)
        if avancada == 'P':
            return num1 ** num2
        else:
            print('Operação invalida!')
print('=-'*10,'\nCALCULADORA AVANÇADA\n', '=-'*10)
num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))
avancada = input('Operação basica ou avancada: ')
if avancada == 'basica':
    operacao = input('Digite a operação \n(+) Soma\n(-) Subtração\n(*) Multiplicação\n(/) Divisão\n: ')
    resultado = calculadora_avancada(num1, num2, operacao)
    print(f'Resultado: {resultado:.2f}')
elif avancada == 'avancada':
    avancada = input('Escolha\n(X) Raiz quadrada\n(P) Potenciação\n: ')
    resultado = operacao_avancada(avancada)
    print(f'Resultado {resultado:.2f}')
''' #Calculadora avançada

'''
#Crie uma função chamada calculadora_com_historico que atua como uma calculadora
#que mantém um histórico das operações realizadas. A função deve aceitar dois números e
#uma operação (adição, subtração, multiplicação, divisão) como entrada. Ela deve retornar o
#resultado da operação. Além disso, a função deve armazenar cada operação realizada em
#uma lista, juntamente com os números e o resultado. O usuário pode optar por consultar o
#histórico das operações. Crie uma função separada para exibir o histórico.

historico = [] #lista vazia
def calculadora_com_historico(): #Função vazia
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    operacao = input('Digite a operação \n(+) Soma\n(-) Subtração\n(*) Multiplicação\n(/) Divisão\n: ')

    if operacao == '+':
         resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        resultado = num1 / num2
    else:
        return 'Operação invalida'
    historico.append(f'{num1} {operacao} {num2} = {resultado}') # Adiciona unidade no final da lista
    print(f'Resultado: {resultado}')
    storage = input('Deseja ver o histórico?\n(S) Sim\n(N) Não\n: ')
    if storage == 'S' or storage == 's':
        for operacao in historico:
            print(operacao)
    if storage == 'N' or storage == 'n':
        print('Próxima operação.')
    calculadora_com_historico()
calculadora_com_historico()
 #Calculadora com histórico
''' #Calculadora com Historico

#6. Crie uma função chamada converte_temperatura_com_registro que realiza conversões de
#temperatura entre Celsius e Fahrenheit, como nas atividades anteriores. No entanto, a
#função deve permitir ao usuário escolher realizar várias conversões consecutivas e manter
#um registro de todas as conversões realizadas em um dicionário, onde as chaves são as
#temperaturas originais e os valores são as temperaturas convertidas. O usuário pode optar
#por consultar o registro a qualquer momento.

def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def converte_temperatura_com_registro():
    registro = {}  # Dicionário para armazenar as conversões
    opcao = ""

    while opcao != "sair":
        print("Escolha uma opção:")
        print("1 - Celsius para Fahrenheit")
        print("2 - Fahrenheit para Celsius")
        print("3 - Consultar registro")
        print("Digite 'sair' para sair")

        opcao = input("Opção: ")

        if opcao == "1":
            celsius = float(input("Digite a temperatura em Celsius: "))
            fahrenheit = celsius_para_fahrenheit(celsius)
            registro[celsius] = fahrenheit
            print(f"{celsius} graus Celsius equivalem a {fahrenheit} graus Fahrenheit.")

        elif opcao == "2":
            fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
            celsius = fahrenheit_para_celsius(fahrenheit)
            registro[fahrenheit] = celsius
            print(f"{fahrenheit} graus Fahrenheit equivalem a {celsius} graus Celsius.")

        elif opcao == "3":
            print("Registro de conversões:")
            for origem, destino in registro.items():
                print(f"{origem} => {destino}")

        elif opcao == "sair":
            print("Encerrando o programa.")

        else:
            print("Opção inválida. Tente novamente.")


# Executando a função
converte_temperatura_com_registro()
        elif opcao == "sair":
            print("Encerrando o programa.")

        else:
            print("Opção inválida. Tente novamente.")


# Executando a função
converte_temperatura_com_registro()