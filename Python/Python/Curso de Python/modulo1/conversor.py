#Crie um módulo chamado `conversor` que tenha funções para converter entre Celsius e
#Fahrenheit.

def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius
