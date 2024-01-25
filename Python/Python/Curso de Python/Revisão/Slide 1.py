"""Desafio 1
1. Crie um programa Python com as seguintes variáveis:
1. Uma variável para armazenar a sua idade.
2. Uma variável para armazenar o seu nome completo.
3. Uma variável para armazenar a cidade em que você mora.
4. Uma variável para armazenar o número de gols marcados por
seu time favorito.
5. Uma constante para armazenar o valor de π (pi) com pelo menos
3 casas decimais.
2. Atribua valores a cada uma das variáveis de acordo com as
informações pessoais (não se preocupe em fornecer informações
reais, isso pode ser fictício).
3. Imprima o valor de cada variável no console.

idade = 25
nome = 'Maksuel da Silva Borges'
cidade = 'Cuiabá-MT'
time = 'SPFC 2 x 0 Flamengo'
PI = 3.141
print(f'Idade: {idade}', f'\nNome: {nome}', f'\nCidade: {cidade}', f'\nTime de futebol: {time}', f'\nPI= {PI}')
"""
"""
1. Calcule a soma de dois números inteiros.
2. Calcule a diferença entre dois números inteiros.
3. Multiplique dois números de ponto flutuante.
4. Divida dois números inteiros e arredonde o resultado para o 
número inteiro mais próximo.
5. Calcule a potência de um número elevado a outro número.

x = 5
y = 9

multiplicar = x * y
dividir = x / y
potencia = x ** 2

print(f'Multiplicação: {multiplicar}', f'\nDivisão: {dividir:.1f}', f'\nPotencia: {potencia}')
"""
"""
1. Verifique se um número é igual a outro número. 
2. Verifique se um número é maior que outro número. 
3. Verifique se uma string é igual a outra string.
4. Verifique se um número é menor ou igual a outro número. 
5. Verifique se duas strings são diferentes.

x = 8
y = 3
z = 'diferente'
z2 = 'diferente 777'

igual = x == y
maior = x > y
menor = x < y
txt_igual = z == z2
maior_igual = x >= y
menor_igual = x <= y
txt_diferente = z != z2

print(f'Numero 8 e 3 São?', f'\n\tIguais: {igual}', f'\n\tMaior: {maior}', f'\n\tMenor: {menor}', f'\n\tTexto igual: {txt_igual}', f'\n\tTexto diferente: {txt_diferente}', f'\n\tMaior ou igual: {maior_igual}', f'\n\tMenor ou igual: {menor_igual}')
#Não sei se é para dar entrar de um numero
"""
'''
1. Crie uma expressão lógica que seja verdadeira se um número for 
maior que 5 e menor que 10.
2. Crie uma expressão lógica que seja verdadeira se uma string não 
estiver vazia.
3. Crie uma expressão lógica que seja verdadeira se um número for 
par (use o operador % para verificar a paridade).
'''
x = 5
y = 10

maior = x <= y
str = 5 == 5 #ta errado isso aqui!
par = y % 2 == 0
print(f'\tMaior: {maior}', f'\n\ttexto: {str}', f'\n\tPar: {par}')
#tem algo de errado aqui!
'''
1. Converta um número inteiro em uma string.
2. Converta uma string que representa um número em um número de 
ponto flutuante.
3. Converta um número de ponto flutuante em um número inteiro 
(arredondando para baixo).
4. Converta uma string que representa um número em um número inteiro.
5. Converta um número inteiro em um número de ponto flutuante. 
6. Converta um número de ponto flutuante em uma string.
7. Converta um número inteiro em uma string e, em seguida, converta essa 
string de volta para um número inteiro.

n = 8
texto = str(n)
numero_float = str(float(n))
'''