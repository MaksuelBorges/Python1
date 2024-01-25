#Faça um programa em que o usuário digita uma série de números reais (float) e, em seguida, recebe as seguintes informações sobre a série de números digitados:
#A média dos números
#A mediana dos números
#Não é permitido utilizar métodos de lista além de len e append.

lista = [] #Lista vazia
n = int(input('Digiete quantidade de itens na lista: '))
#Obtem os valores
for i in range(n):
    v = float(input('Digite um valor:'))
    lista.append(v)
#Calcula o somatorio
soma = 0
for v in lista:
    soma += v
#Calcula a média
media = soma / n
lista.sort()
if n % 2 == 0: # se o elemento é par
    mediana = (lista[n // 2] + lista[n // 2 + 1]) / 2
    mediana = lista[n//2]
else: # se nao, n for impar.]
    mediana = lista[n // 2]
print(lista)
print(f'Media: {media}')
print(f'Mediana: {mediana}')