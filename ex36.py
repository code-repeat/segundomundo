valor_casa = float(input('Valor da casa: '))
salario_cliente = float(input('Informe o salário do cliente: '))
anos = int(input('Em quantos anos deseja parcelar: '))

meses = anos * 12
valor_parcela = valor_casa / meses

if valor_parcela > (salario_cliente * 30) / 100:
    print('Seu empréstimo foi negado')
    print('O valor da parcela de R${:.2f} excede 30% do seu salário atual.'.format(valor_parcela))
else:
    print('Valor da casa ............R${}'.format(valor_casa))
    print('Quantidade de parcelas: ............{}x'.format(meses))
    print('Valor das parcelas (sem juros).......R${:.2f}'.format(valor_parcela))

