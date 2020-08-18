frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
tudo_junto = ''.join(palavras)
inverso = tudo_junto[::-1]
if inverso == tudo_junto:
    print('O inverso de {} é {}'.format(tudo_junto, inverso))
else:
    print('A frase digitada não é um palíndromo')

