#1 Imprima a data e hora atuais.
import datetime

agora = datetime.datetime.now()
print(agora)

#2 Crie um objeto `datetime` com a data de nascimento de uma pessoa e calcule quantos dias de vida ela tem.
import datetime

nasceu = datetime.date(1990, 5, 25)
atual = datetime.date(2023, 11, 1)
diferenca = atual - nasceu
print(nasceu)
print(diferenca.days)

#3
def diferenca_em_dias(data1,data2):
    diferenca = abs((data1,data2).days)
    return diferenca
date_a = datetime.datetime()