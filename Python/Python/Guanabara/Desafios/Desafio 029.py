#Escreve um programa que leia uma velocida de de um carro. Se ele ultrapasar 80km/h, mostre uma menssagem dizendo que
#ele foi multado. A multa vai custar R$7.00 a cada KM acima da velocidade.

radar = float(input('Radar de Varzeagrande. Você passou há: '))
if radar>=81:
    print('Você foi multado!!! está acima da velodade permitida')
    print(f'Sua multa é {(radar-80)*7}')
else:
    print ('')
