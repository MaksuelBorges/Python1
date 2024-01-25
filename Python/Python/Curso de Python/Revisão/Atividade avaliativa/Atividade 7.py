'''
#Verificação de Paridade: Peça ao usuário para inserir um número inteiro e, em seguida, verifique se o número
#é par ou ímpar. Imprima o resultado.

num = int(input('Digite um numero inteiro para saber se é par ou impar: '))
if num % 2 == 0: # Numero divido por 2 e o resto for 0
    print(f'O numero {num} é par.')
elif num % 3 == 0: # Numero divido por 3 e o resto for 0
    print(f'O numero {num} é impar.')
'''
'''
#Validação de Idade: Solicite ao usuário que insira sua idade. Em seguida, verifique se
#a idade está dentro de um intervalo válido (por exemplo, entre 18 e 65 anos).
#Imprima se a idade é válida ou não.

idade = int(input('Digite sua idade: '))
if idade <=17:
    print('Você tem muito o que viver ainda.')
elif idade >=18 and idade <= 60:
    print('Você está na melhor fase da vida.')
else:
    print('Se arrepende de algo?')
'''
'''
#Login Simples: Crie um programa que simule um login simples. Peça ao usuário para inserir um nome de usuário e uma senha.
#Em seguida, verifique se o nome de usuário e a senha correspondem a um par específico predefinido por você. Imprima uma mensagem de sucesso ou falha.

usr = input('Usuário: ')
pw = input('Senha: ')
if usr == pw:
    print('O usuário não pode ser igual a senha!')
else:
    print(f'Usuário: {usr}\nSenha: {pw}\n### Cadastro feito com SUCESSO!!! ###')
'''
'''
#Triângulo Retângulo: Peça ao usuário para inserir três comprimentos de lados. Verifique se esses comprimentos podem
#formar um triângulo retângulo (onde a soma dos quadrados dos dois lados menores é igual ao quadrado do lado mais longo).
#Imprima se é um triângulo retângulo ou não.

print('Insira três valores para criar um triângulo.')
b = float(input('Primeiro base: '))
b2 = float(input('Segundo base: '))
a = float(input('Terceiro altura: '))
if b ** 2 + b2 ** 2 == a ** 2:
    print('Estes valores forma um Triangulo retangulo.')
else:
    print('Estes valores não formam um triangulo')
'''
'''
#Verificação de Divisibilidade: Solicite ao usuário para inserir um número. Verifique se esse número é divisível por 3 e 5 ao mesmo tempo. Imprima o resultado.

num = int(input('Digite um Numero: '))
if num % 3 == 0 and num % 5 == 0: #Na estrutura, sempre vai ser a primeira possibilidade você não pode ter ambos.
    print('Este numero é multiplo por ambos 3 e 5.')
elif num % 3 == 0:
    print('Este numero é multiplo de 3.')
elif num % 5 == 0:
    print('Este numero é multiplo por 5.')
#tentei coloar um "elif num % 3 == 0 and num % 5 == 0:" no final e o programa não leu. Porque se ele é multimplo de um ou do outro já é por ambos.
else:
    print('Esse numero não é multiplo de 3 ou de 5.')
'''