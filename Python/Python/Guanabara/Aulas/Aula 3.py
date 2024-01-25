#int = números inteiros ex: 1,2,3,4,5,6.. -2,-3,-4,0...
#float = números reais ou numero de ponto flutuante ex: 4.6, 7.9,0.002....
#bool = valores logicos ou boleanos ex: True, False
#str = caracteres ou strings ex: 'abncefghi..' tudo entre ''

numero1=int(input("Digite um numero: "))
numero2=int(input("Digite outro numero: "))
soma=numero1+numero2
#print('A soma entre',numero1,'e',numero2,'é: ',soma)
print('A soma entre {} e {} vale: {}'.format(numero1, numero2, soma))

