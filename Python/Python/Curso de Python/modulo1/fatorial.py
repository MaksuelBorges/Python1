#Crie um módulo chamado `fatorial` com uma função que calcula o fatorial de um número.

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
#num = int(input('Informe um numero: '))
#print(fatorial(num))