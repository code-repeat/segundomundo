peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)
if imc < 18.5:
    print('IMC: {:.1f} > Você está abaixo do peso.'.format(imc))
elif imc > 18.5 and imc <= 25:
    print('IMC: {:.1f} > Você está com peso ideal.'.format(imc))
elif imc > 25 and imc <= 30:
    print('IMC: {:.1f} > Você está na categoria sobrepeso.'.format(imc))
elif imc > 30 and imc <= 40:
    print('IMC: {:.1f} > Você está obeso.'.format(imc))
elif imc > 40:
    print('IMC: {:.1f} > Cuidado! Obesidade mórbida!.'.format(imc))