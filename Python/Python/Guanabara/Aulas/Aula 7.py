#===========================Aula 7 só teoria!=========================
'''
####### Operadores aritmeticos#########
+ ADIÇÃO >>>> adição, soma
- SUBTRAÇÃO >>>> Subtração,
* MULTIPLICAÇÃO >>>> Multiplica
/ DIVISÃO >>>> Dividir
** POTÊNCIA >>>> exponenciação ou potencia
// DIVISAO INTEIRA >>>> ""
% RESTO DA DIVISÃO >>>> ""
**(1/2) >>> Rais quadra
########################################

!!!!!! UM SIMBOLO DE = É O SINAL DE ATRIBUIÇÃO, lê-se "Recebe"!!!!!!!!!!!!!

Adição 5+2== 7
Subtração 5-2== 3
Multiplicação 5*2== 10
Divisão 5/2== 2.5 <<< Numero flutuante (float)
Potencia 5**2== 25  5
Divisão inteira 5//2== 2 <<< O inteiro da divisão
Resto da divisão 5%2== 1 <<< O resto da divisão.. não tem como dividir 1 nesse caso

==========ORDEM DE PRECEDÊNCIA=======

1- () << parenteses. Pode-se ter parenteses dentro de parenteses.
2- ** << potencia. Segunda coisa mais importante dentro de uma expressao.
3- *, /, //, % << Faz quem aparecer primeiro!
4- +, - << por ultimo na ordem.
!!!! EXECUTAR UM PROGRAMA E FUNCIONAR, PODE NÃO ESTAR CERTO!  !!!!!!!

EXEMPLO!!!!!!!!!!!!!!!

5+3*2== 11 << Primeiro a multiplicação
3*5+4**2== 31 << Primeiro potencia depois multiplicação por fim soma.
3*(5+4)**2== 243 << Primeiro parenteses depois a potencia por fim multiplicação.

end=''<<<<< NÃO QUEBRA A LINHA, O PRINT FICA NA MESMA LINHA!!!
\n <<<< NOVA LINHA ELE QUEBRA A LINHA

'''
'''
nome = input('Qual seu nome? ')
print(f'Prazer em te conhecer {nome:=^30}')
'''
############## Variaveis ################ Toda variavel é um objeto. Um objeto é um pouco mais que uma variavel!
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
p = n1**n2

print(f'A soma é {s}, o produto é {m} e a divisão é {d:.3f}') # Nesse caso é uma soma direta! vai mostrar só nesse ponto.
print(f'Divisão inteira {di} e potência {p}')