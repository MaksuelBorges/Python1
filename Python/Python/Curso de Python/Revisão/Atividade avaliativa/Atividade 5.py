'''
Converta um número inteiro em uma string.
Converta uma string que representa um número em um número de ponto flutuante.
Converta um número de ponto flutuante em um número inteiro (arredondando para baixo).
Converta uma string que representa um número em um número inteiro.
Converta um número inteiro em um número de ponto flutuante.
Converta um número de ponto flutuante em uma string.
Converta um número inteiro em uma string e, em seguida, converta essa string de volta para um número inteiro.
'''
#Variaveis globais
numero = int(10)
numero_string = str(numero)
numero_flutuante = float(numero_string)
arredondamento = float(round(numero_flutuante - 0.5))
string_inteiro = int(numero_string)
xflutuante =  float(string_inteiro)
xstring = str(xflutuante)
xinteiro = (int(str(int(numero))))
#Impressão e tipagem
print(f'Numero: {numero}', type(numero))
print(f'String: {numero}',type(numero_string))
print(f'Flutuante: {numero}', type(numero_flutuante))
print(f'Arredondamento para baixo: {numero}', type(arredondamento))
print(f'String que repesenta um numero inteiro: {numero}', type(string_inteiro))
print(f'Numero inteiro em flutuante: {numero}', type(xflutuante))
print(f'Numero flutuante em string: {numero}', type(xstring))
print(f'Numero inteiro em String depois em numero inteiro: {numero}', type(xinteiro))