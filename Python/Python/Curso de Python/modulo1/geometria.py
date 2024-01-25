#Crie um módulo chamado `geometria` com funções para calcular a área e perímetro de um
#quadrado, retângulo, círculo e triângulo.

def area_quadrado(lado):
    return lado * lado

def perimetro_quadrado(lado):
    return 4 * lado

def area_retangulo(comprimento, largura):
    return comprimento * largura

def perimetro_retangulo(comprimento, largura):
    return 2 * (comprimento + largura)

def area_circulo(raio):
    return 3.14159 * (raio ** 2)

def perimetro_circulo(raio):
    return 2 * 3.1459 * raio

def area_triangulo(base, altura):
    return 0.5 * base * altura

def perimetro_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3