#1: Tupla de Coordenadas Criar uma tupla com coordenadas (latitude, longitude) de uma cidade. Exibir as coordenadas da cidade.
# Tentar atualizar as coordenadas (isso não deve funcionar, pois as tuplas são imutáveis).
#2: Tupla de Números de Telefone Criar uma tupla com números de telefone de emergência. Exibir os números de telefone.
#Tentar adicionar um novo número de telefone (não é possível devido à imutabilidade das tuplas).
#3: Tupla de Dias da Semana Criar uma tupla com os dias da semana. Exibir o primeiro dia da semana. Tentar reorganizar
#os dias da semana (não é possível devido à imutabilidade das tuplas).

dic = {'nome': 'Maks', 'Idade': 24}
for chave in dic:
    valor = dic[chave]
    print(f'{chave} {valor}:')