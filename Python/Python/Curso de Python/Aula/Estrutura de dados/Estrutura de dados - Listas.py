#1: Lista de Números Inteiros Criar uma lista de números inteiros de 1 a 10. Exibir a lista na ordem original.
#Classificar a lista em ordem crescente e exibi-la novamente.
#2: Lista de Nomes de Cores Criar uma lista de nomes de cores (por exemplo, "vermelho", "azul", "verde"). Adicionar uma
#nova cor à lista. Remover uma cor da lista e exibi-la novamente.
#3: Lista de Tarefas Diárias Criar uma lista de tarefas diárias. Mostrar a primeira tarefa da lista. Marcar a primeira tarefa como concluída e removê-la da lista.

#lista em sua forma original
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)

list_cor = ['vermelho', 'azul', 'verde', 'branco']
list_cor.append('preto') # Adiciona um elemento ao final da lista
print(list_cor)
list_cor.pop(1) #Remove o indice da lista no caso azul.
print(list_cor)

task = ['lavar', 'limpar', 'arrumar', 'almoço']
print(task[0], 'Concluida') # Imprimindo somente o item 0 da lista com uma menssagem concluida
task.pop(0)
print(task) #Imprimiu a lista só que removendo o primeiro item.