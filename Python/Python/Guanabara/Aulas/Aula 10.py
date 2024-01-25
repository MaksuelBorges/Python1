# Condinções simples e compostas#
'''
carro.siga()
carro.esquerda()
carro.siga()
carro.direita()

##Comandos sequenciais## sempre de CIMA para BAIXO. Da esquerda para direita.
Agora se tem possibilidades dentro do programa. Tomar uma descisão anula outra
e cria condições
Dentro de um mesmo se tem um outro programa diferete.
!!!!!!
SE

SENÃO
!!!!!!

Analogia!!!
carro.siga()
SEcarro.esquerda()   -> sem indentação, significa que vai acontecer todas as vezes. Colado na parede*
    carro.siga()           }
    carro.direita()        }
    carro.siga()           }
    carro.direta()         } INDENTAÇÃO: afastados por espaço da margem e dispostos hierarquicamente, para facilitar a visualização e percepção do programa.
    carro.esquerda()       }
    carro.siga()           }
    carro.direita()        }
    carro.siga()           }
SENÃO
    carro.siga()           }
    carro.esquerda()       }
    carro.siga()           } INDENTAÇÃO :afastados por espaço da margem e dispostos hierarquicamente, para facilitar a visualização e percepção do programa.
    carro.esquerda()       }
    carro.siga()           }
carro.pare()

SEcarro.esquerda()        IF
    Bloco verdadeiro
SENÃO                     ELSE
    Bloco falso
#### ESTRUTURA CONDICIONAL### nunca vai ser usado ambos, ou true ou false
IFcarro.esquerda():
    Bloco verdade
ELSE:
    Bloco falso
EX:
tempo=int(input('Quantos anos tem seu carro?'))
inf tempo <=3:
    print('carro novo!')
else:
    print('carro velho')
print('--FIM--')

'''
'''nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo voce tem!')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia, {nome}')
'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi: {m:.1f}')
if m>=6.0:
    print('Sua média foi boa! Parabens!')
else:
    print('Sua média foi ruim! Estude mais!')
