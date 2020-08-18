pesos = []
for p in range(1, 6):
    peso = float(input('Peso {}: '.format(p)))
    pesos += [peso]
print(f'O maior peso digitado foi {max(pesos)}kg')
print(f'O menor peso digitado foi {min(pesos)}kg')
