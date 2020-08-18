n = int(input('Digite um número: '))
fatorial = 1
count = 1

while count <= n:
    fatorial *= count
    count += 1
print(fatorial)
