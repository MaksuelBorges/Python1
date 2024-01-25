'''
1. Crie uma expressão lógica que seja verdadeira se um número for maior que 5 e menor que 10.
2. Crie uma expressão lógica que seja verdadeira se uma string não estiver vazia.
3. Crie uma expressão lógica que seja verdadeira se um número for par (use o operador % para verificar a paridade).
'''
numero = 6
string = 'vazia?'
numero3 = 12
#Exercicio1 numero puxa 6 que é maior que 5 e menor que 10
e_logica = 5 < numero < 10
print(f'Expressão lógica: {e_logica}')
#Exercico2 string como variavel puxa a string 'vazia?' usando bool mostrando verdade que o texto não está vazio.
e_logica2 = bool(string)
print(f'Expressão lógica: {e_logica2}')
#Exercico3 numero3 puxa a variavel 12 que é um numero par aleatorio divisivel por 2 com resto 0.
par = numero3 % 2 == 0
print(f'Expressão lógica: {par}')