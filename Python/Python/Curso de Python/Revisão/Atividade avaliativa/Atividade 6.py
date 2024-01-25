'''
#Atividade 1: Verificação de Paridade Peça ao usuário para inserir um número inteiro. Em
#seguida, verifique se o número é par ou ímpar e exiba a mensagem apropriada.

num = int(input('Digite um numero para verificar se é Par ou Impar: '))
if num % 2 == 0:
    print(f'Numero par: {num}')
else:
    print(f'Numero impar: {num}')

'''
'''
#Atividade 2: Verificação de Idade Peça ao usuário para inserir sua idade. Com base na idade, exiba mensagens diferentes, como "Criança", "Adolescente" ou "Adulto".
idade = int(input('Digite Sua idade: '))
if idade <= 12:
    print('Você é uma criança ainda!!!')
elif idade >= 13 and idade <= 18:
    print('Você é um adolecente!!!')
else:
    print('Você já é um adulto!!!')
    
'''
'''
#Atividade 3: Verificação de Múltiplos Peça ao usuário para inserir um número. Verifique se o número é múltiplo de 3, de 5 ou de ambos, e exiba as mensagens apropriadas.

num = int(input('Digite um Numero: '))
if num % 3 == 0 and num % 5 == 0: #Na cadeia, sempre você a primeira possibilidade você não pode ter ambos.
    print('Este numero é multiplo por ambos 3 e 5.')
elif num % 3 == 0:
    print('Este numero é multiplo de 3.')
elif num % 5 == 0:
    print('Este numero é multiplo por 5.')
#tentei coloar um "elif num % 3 == 0 and num % 5 == 0:" no final e o programa não leu. Porque se ele é multimpo de um ou do outro já é por ambos.
else:
    print('Esse numero não é multiplo de 3 ou de 5.')
    
'''
'''
#Atividade 4: Notas em Letras Peça ao usuário para inserir uma nota de 0 a 100. Converte a nota para o sistema de letras (A, B, C, D, F) com base nas notas padrão.

nota = int(input('Digite um numero de 0 a 100 para sabe sua nota em letra: '))
if nota < 21:
    print(f'Sua nota é um F!!! \nVocê não está estudando?')
elif nota >= 21 and nota <= 40:
    print(f'Sua noda é D!!! \nEstá estudando muito pouco.')
elif nota >= 41 and nota <= 60:
    print('Sua nota é um C!!! \nVocê precisa estudar mais, está no caminho')
elif nota >=61 and nota <= 80:
    print('Sua nota é B!!! \nVocê estudou bem, vamos chegar ao topo!!!')
else:
    print('Sua nota é um A!!!\nMaravilha!!! o topo é aqui, mas não pode parar!!!\nAqui é só o começo')
    
'''
'''
#Atividade 5: Calculadora de IMC Peça ao usuário para inserir seu peso e altura. Com base nesses
#valores, calcule o Índice de Massa Corporal (IMC) e forneça uma interpretação do resultado.

print('\n########## VAMOS CALCULAR O SEU (IMC) Indice de Massa Corpotal ##########\n\n')
#Váriaveis globais
nome = input('Digite seu nome: ')
idade = input('Qual sua idade: ')
altura = float(input('Qual sua altura: '))
peso = float(input('Qaul seu peso: '))
#Estrutura
imc = peso / (altura * altura)
if imc < 18.5:
    print(f'Nome: {nome}\nIdade: {idade}\nAltura: {altura}\nPeso: {peso}kg\nIMC: {imc:.1f}\nSua Classificação: Magreza')
elif imc >= 18.6 and imc <= 24.9:
    print(f'Nome: {nome}\nIdade: {idade}\nAltura: {altura}\nPeso: {peso}kg\nIMC: {imc:.1f}\nSua Classificação: Normal')
elif imc >= 25 and imc <=29.9:
    print(f'Nome: {nome}\nIdade: {idade}\nAltura: {altura}\nPeso: {peso}kg\nIMC: {imc:.1f}\nSua Classificação: Sobrepeso')
elif imc >= 30 and imc <= 34.9:
    print(f'Nome: {nome}\nIdade: {idade}\nAltura: {altura}\nPeso: {peso}kg\nIMC: {imc:.1f}\nSua Classificação: Obesidade grau I')
elif imc >= 35 and imc <= 39.9:
    print(f'Nome: {nome}\nIdade: {idade}\nAltura: {altura}\nPeso: {peso}kg\nIMC: {imc:.1f}\nSua Classificação: Obesidade grau II')
else:
    print(f'Nome: {nome}\nIdade: {idade}\nAltura: {altura}\nPeso: {peso}kg\nIMC: {imc:.1f}\nSua Classificação: Obesidade grau III')
'''
'''
#Atividade 6: Classificação de Triângulos Peça ao usuário para inserir os comprimentos dos lados de um triângulo.
#Classifique o triângulo como "Equilátero" (todos os lados iguais), "Isósceles" (dois lados iguais) ou "Escaleno" (todos os lados diferentes).

print('Informe 3 valores para verifcar se é um triangulo equilate, isósceles ou escaleno.\n')

a = float(input('Comprimento de um lado: '))
b = float(input('Comprimento de um outro lado: '))
c = float(input('Por fim comprimento de um terceiro lado: '))
# A soma de quaisquer 2 lado tem que ser menor que o terceiro lado, caso contrario não se forma um triangulo.
if (a + b < c) or (a + c <b) or (b + c < a):
    print('Estes valaores não formam um triangulo')
elif (a == b) and (a == c):
    print('Triangulo equilatero!')
elif (a == b) or (a == c) or (c == b):
    print('Este é um triangulo isóseles!')
else:
    print('Triangulo escaleno!')
'''
'''
#Atividade 7: Conversão de Moedas Peça ao usuário para inserir uma quantidade em uma moeda (por exemplo, dólares) e, com
#base em uma taxa de câmbio, converta a quantia para outra moeda (por exemplo, euros).

print('Cambio do dólar atual em comparação ao real: 5,032\n')
i = float(input('Converter real para dólar.\nValor: '))
valor = i * 5.032
print(f'{valor:.3f} Dólares.')
'''
'''
#Atividade 8: Comparação de Três Números Peça ao usuário para inserir três números. Encontre e exiba o maior número.
print('Insira tres numeros para ver qual é maior.\n')
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
n3 = int(input('Terceiro numero: '))
if n1 > n2 > n3:
    print(f'Primeiro numero maior: {n1}')
elif n1 < n2 > n3:
    print(f'Segundo numero maior: {n2}')
else:
    print(f'Terceiro numero maior: {n3}')
'''
'''
#Atividade 9: Calculadora Simples Crie uma calculadora simples que permite ao usuário escolher
#uma operação (adição, subtração, multiplicação, divisão) e realizar o cálculo com dois números
#fornecidos.

print('Calculadora simples.\n')
resultado = 0
num1 = int(input('Numero: '))
operacao = input('(+) Somar\n(-) Subtrair\n(*) Multiplicar\n(/) Dividir\n: ')
num2 = int(input('Numero: '))
somar = num1 + num2
subtrair = num1 - num2
multiplicar = num1 * num2
dividir = num1 / num2
if operacao == '+':
    resultado = somar
    print(f'\nResultado: {resultado}')
elif operacao == '-':
    resultado = subtrair
    print(f'\nesultado: {resultado}')
elif operacao == '*':
    resultado = multiplicar
    print(f'\nResultado: {resultado}')
elif operacao == '/':
    resultado = dividir
    print(f'\nResultado: {resultado}')
else:
    print('\nOperação invalida!')
'''
'''
#Atividade 10: Verificação de Vogais Peça ao usuário para inserir uma letra. Verifique se a letra é
#uma vogal (a, e, i, o, u) e exiba a mensagem apropriada.

letra = input('Digite uma letra:')
#usei uma lista aprendida em uma aula pra frente.
if letra in ['a', 'e', 'i', 'o', 'u'] or letra in ['A', 'E', 'I', 'O', 'U']:
    print('Vogal')
else:
    print('Não é vogal')
'''
'''
#Atividade 11: Classificação de Idade Peça ao usuário para inserir a idade. Classifique a idade em "Criança"
# "Adolescente", "Adulto" ou "Idoso" com base em critérios de faixa etária.
idade = int(input('Digite Sua idade: '))
if idade <= 19:
    print('Você é um Adolescente!!!')
elif idade >= 20 and idade <= 59:
    print('Você é um Adulto!!!')
else:
    print('Você já é um Idoso!!!')
'''
'''
#Atividade 12: Verificação de Ano Bissesto Peça ao usuário para inserir um ano. Verifique se o ano é bissexto e explique o resultado.

ano = int(input('Insira um ano para verificar se é bissexto: '))
if ano % 4 == 0:
    print('Ano Bissexto!')
else:
    print('Não é um ano bissexto')
'''
'''
#Atividade 13: Menu de Restaurante Crie um menu de restaurante com vários itens e preços. Peça ao usuário para escolher
#um item e, com base na escolha, calcule o valor total.

print('###### MENU ######')
print('(1) Pizza R$79,99\n(2) Coca-cola R$13,00\n(3) Alcatra R$42,00\n(4) Carvão R$15,00\n(5) Gelo R$11,00\n')
menu = int(input('Escolha um número do menu: '))
if menu == 1:
    item = 'Pizza'
    preco = 79.99
elif menu == 2:
    item = 'Coca-cola'
    preco = 13.00
elif menu == 3:
    item = 'Alcatra'
    preco = 42.00
elif menu == 4:
    item = 'Carvão'
    preco = 15.00
elif menu == 5:
    item = 'Gelo'
    preco = 11
else:
    print('Essa opção não tem no menu!!')
    item = 0
if item:
    menu = int(input(f'Quantidade de {item} que você deseja? '))
    total = preco * menu
    print(f'Total a pagar: {total}')
'''
'''
#Atividade 14: Avaliação de Notas Peça ao usuário para inserir notas de um aluno e calcule a
#média. Com base na média, forneça uma avaliação, como "Aprovado" ou "Reprovado".

nota1 = float(input('Nota de Matematica: '))
nota2 = float(input('Nota de Portugues: '))
nota3 = float(input('Nota de Ingles: '))
nota4 = float(input('Nota de Fisica: '))
nota5 = float(input('Nota de Quimica: '))
media = (nota1+nota2+nota3+nota4+nota5) / 2
print(f'Nota: {media}')
if media <= 14.75: # Se a media for menor ou igual a 14.75
    print('O aluno está Reprovado')
else:
    print('O aluno está Aprovado')
'''
#Atividade 15: Calculadora de Juros Crie uma calculadora de juros simples que permite ao usuário
#inserir o valor principal, a taxa de juros e o período. Calcule o montante final e exiba-o.

print('Cauculadora de juros\n') #juros por mes
dinheiro = float(input('Quanto dinheiro tem? '))
tjuros = float(input('Quantos % está o juros? '))
tempo = float(input('Quantos meses? '))
juros = dinheiro * (tjuros / 100) * tempo #
print(f'\nO dinheiro rendeu: {juros:.2f}')
print(f'O montande é {dinheiro+juros:.2f}')