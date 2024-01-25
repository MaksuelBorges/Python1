#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

v = float(input('Entre com um valor em metros para converter em centrimetros e milimetros: '))
c = v*100
m = v*1000
print(f'Metros: {v}m',f'\nCentimetros: {c}cm',f'\nMilimetros: {m}mm')
