r1 = float(input('Valor da primeira reta: '))
r2 = float(input('Valor da segunda reta: '))
r3 = float(input('Valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('Você formou um triângulo EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('Você formou um triângulo ESCALENO!')
    else:
        print('Você formou um triângulo ISÓSCELES!')
else:
    print('Não foi possível criar um triângulo')