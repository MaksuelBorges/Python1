print('Opções:\n1 = Escreve guilherme\n2 = Escreve Joao\n3 = Escreve maria')

opcao = input('Escolha um opção: ')

if opcao == '1':
    print('Guilherme')
elif opcao == '2':
    print('João')
elif opcao == '3':
    print('Maria')
else:
    print('Opcao invalida!')

#print(not True) #Não verdadeira é falso
idade = 50

if idade == 50:
    print('Voce tem 50 anos')
else:
    print('Voce nao tem 50 anos')

if True:
    print('Entrou no if')
else:
    print('Entrou no else')