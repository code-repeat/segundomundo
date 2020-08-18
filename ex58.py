from random import randint
cerebroComputador = randint(0, 10)
palpite = int(input('''
Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você conseguiria advinhar?
Qual é seu palpite? '''))
numeroPalpites = 1

while palpite != cerebroComputador:
    if palpite > cerebroComputador:
        print('Menos... Tente mais uma vez')
        palpite = int(input('Qual é seu palpite? '))
    else:
        print('Mais... Tente mais uma vez')
        palpite = int(input('Qual é seu palpite? '))
    numeroPalpites += 1

print(f'Acertou com {numeroPalpites} tentativas. Parabéns!')

