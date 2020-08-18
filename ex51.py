a = int(input('Digite o primeiro termo de sua P.A: '))
r = int(input('Digite a razão de sua P.A: '))
decimo = a + (10 - 1) * r
for p in range(a, decimo + r, r):
    print(f'{p}', end=' ')