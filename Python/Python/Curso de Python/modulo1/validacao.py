#Crie um módulo chamado `validacao` que tenha uma função para verificar se um número é
#primo.

def num_primo(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if n % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True