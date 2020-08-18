nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2
if media < 5.0:
    print('Sua média é {:.1f}. VOCÊ ESTÁ REPROVADO!'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('Sua média é {:.1f}. VOCÊ ESTÁ EM RECUPERAÇÃO!'.format(media))
else:
    print('Sua média é {:.1f}. VOCÊ ESTÁ APROVADO!'.format(media))