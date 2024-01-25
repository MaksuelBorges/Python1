#Crie um módulo chamado `fibonacci` com uma função que gera a sequência de Fibonacci
#até o enésimo termo.

fibonanacci = [1,1]
while len(fibonanacci) < n:
    proximo_termo = fibonanacci[-1] + fibonanacci[-2]
    fibonanacci.append(proximo_termo)
return fibonanacci