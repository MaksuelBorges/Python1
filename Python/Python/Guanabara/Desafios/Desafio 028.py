#Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5
#e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador
#O programa devera escrever na tela se venceu ou perdeu.


p = int(input("Qual numero estou pensando? entre 0 e 5: "))
if p == 2:
    print("Parabéns!!! Você acertou")
else:
    print("Bocó errou, Ganhei!!")
