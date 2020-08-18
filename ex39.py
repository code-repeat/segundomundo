from datetime import date
ano_nascimento = int(input('Digite o ano em que você nasceu: '))
idade = date.today().year - ano_nascimento

if idade == 18:
    print('Você tem {} anos e já está na hora certa de se alistar!'.format(idade))
elif idade < 18:
    tempo_restante = 18 - idade
    print('Você tem {} anos. Ainda faltam {} anos para você se alistar'.format(idade, tempo_restante))
else:
    tempo_ultrapassado = idade - 18
    print('Você já passou do prazo de alistamento! Você tem {} anos e já passou {} anos do prazo determinado'.format(idade, tempo_ultrapassado))
