#Exercício 2: Crie uma função que divide dois números e trate o erro se o divisor for zero.
def divisao (numero1, numero2):
    try:
        resultado = numero1 / numero2
        return resultado
    except ZeroDivisionError:
        return 'Erro: Divisao por zero. Nao é possivel dividir por zero'

#Exemplo
print(divisao(2,2))