'''
#1 Crie um módulo chamado `calculadora` que tenha funções para adição, subtração, multiplicação e divisão.
import calculadora

a = 10
b = 2

print(f'Soma: {calculadora.soma(a,b)}\nSubtração: {calculadora.subtrair(a,b)}\nMultipicação: {calculadora.multiplicacao(a,b)}\nDivisão: {calculadora.divisao(a,b)}')
'''

#2 Crie um módulo chamado `conversor` que tenha funções para converter entre Celsius e Fahrenheit.
from Módulos_I import conversor
celsius = float(input('Quantos graus celsius está fazendo ai em cuiaba:'))
fahrenheit = celsius_para_fahrenheit(celsius)
print(f'Temperatura em Fahrenheit: {fahrenheit}')
