'''
lista = ['Filipe', 'João', 'Matheus'] #expressão para definir uma lista
print(lista[1]) #index da posição na lista

#TRY EXCEPT!!! muito usado em aninhamentos de possiveis erro, falicitando tanto a visualização tanto para o usurario.
try:
    nome = lista[3]
    print(nome)
except Exception as e:
    print('Ocorreu um erro')
'''
'''
lista = ['Filipe', 'João', 'Matheus']
print(lista)
i = int(input('Digite um indice de 0 a 2: '))
lista[i] = 'Ana'
print(lista)
'''
'''
#Adicionando um nume a lista
lista = ['Filipe', 'João', 'Matheus']
print(lista)
lista.append('Ana') #Método append adiciona o 'OBJETO' no final da lista.
lista.insert(0,'Gabi') #Método .insert adiciona o 'OBJETO'no index que desejar somente dentro do range!
del lista[2] #Del remove o index da lista
lista.remove('Filipe') #.remove especifica qual valor voce deseja tirar
lista.pop # Ele vai remorever o ultimo index da lista.
print(lista)
'''
'''
lista = [6, 8, 11, 5, 53, 8]
print(lista)
lista.sort() #Sort organiza a lista. Colocar em orgem
lista.sort(reverse=True) #Coloca em ordem decrescente
print(lista)

count(elemento): Retorna o nuero de ocorrencia de um elemento na lista.
'''

lista = ['A', 'B', 'C', 'D']
for i in range(5):
    print(len(lista)) #retorna o tamanho da lista
    print(lista[i])
