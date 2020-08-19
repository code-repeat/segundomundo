'''from math import factorial
n = int(input('Digite um número: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}')'''

#  Outro método

n = int(input('Informe um número: '))
c = n
f = 1
print(f'Calculando {n}! ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')


