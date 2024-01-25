#Exercício 1: Crie uma função que tente converter uma string em um número inteiro e trate o erro se a
#conversão falhar.
def converter_para_inteiro(string):
    try:
        numero = int(string)
        return numero
    except ValueError:
        return 'Erro: Nao é numero'

#Exemplo
soma = converter_para_inteiro(input('Digite um numero: ' + input('Digite outro numer: ')))
print(soma)