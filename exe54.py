from datetime import date
lista = []
for i in range(1, 8):
    ano_nascimento = int(input('Ano de nascimento {}:'.format(i)))
    lista += [ano_nascimento]

idade = [date.today().year - l for l in lista]
maiores = [ma for ma in idade if ma > 18]
menores = [me for me in idade if me < 18]

print(f'{len(maiores)} pessoa(s) atingiram a maioridade')
print(f'{len(menores)} pessoa(s) ainda são menores de idade')





