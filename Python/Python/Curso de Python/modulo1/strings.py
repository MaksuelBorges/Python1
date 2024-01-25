#Crie um módulo chamado `strings` com funções para contar o número de vogais e
#consoantes em uma string.

def contar_vogais_consoantes(frase):
    vogais = "AEIOUaeiou"
    consoantes = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
    num_vogais = sum(1 for letra in frase if letra in vogais)
    num_consoantes = sum(1 for letra in frase if letra in consoantes)
    return num_vogais, num_consoantes
