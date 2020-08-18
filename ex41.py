from datetime import date
ano_nascimento = int(input('Digite a data de nascimento do participante: '))
idade = date.today().year - ano_nascimento
print(f'Idade: {idade} anos')
if idade <= 9:
    print('Você está na categoria MIRIM!')
elif idade <= 14:
    print('Você está  na categoria INFANTIL!')
elif idade <= 19:
    print('Você está na categoria JUNIOR!')
elif idade <= 25:
    print('Você está na categoria SÊNIOR')
else:
    print('Você está na categoria MASTER!')
