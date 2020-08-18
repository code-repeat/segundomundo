def dinheiro_cheque(n):
    desconto = n - ((n * 10) / 100)
    return desconto

def carta_vist(n):
    desconto = n - ((n * 5) / 100)
    return desconto

def juros(n):
    juro = n + ((n * 20) / 100)
    return juro

valor_produto = float(input('Valor do produto [R$] '))
print('''
    Informe o método de pagamento:
    [1] - Dinheiro
    [2] - Cheque
    [3] - Cartão de Crédito
    [x] - Cancelar a compra
    
''')
metodo_pagamento = str(input('>>> ')).strip()
if metodo_pagamento == '1' or metodo_pagamento == '2':
    print('Valor da compra ............R${:.2f}'.format(valor_produto))
    print('Desconto aplicado ..........10%')
    print('Valor final da compra: R${:.2f}'.format(dinheiro_cheque(valor_produto)))
elif metodo_pagamento == '3':
    print('''
        =-=-=- PAGAMENTO COM CARTÃO DE CRÉDITO -=-=-=
        [d] - Débito (5% de desconto)
        [2] - Parcelar em 2x (preço normal)
        [3] - Parcelar em 3x (20% de juros)
    ''')
    pag_cartao = str(input('>>> ')).strip()
    if pag_cartao == 'd':
        print('Valor da compra ............R${:.2f}'.format(valor_produto))
        print('Desconto aplicado ..........5%')
        print('Valor final da compra: R${:.2f}'.format(carta_vist(valor_produto)))
    elif pag_cartao == '2':
        print('Valor da compra ............R${:.2f}'.format(valor_produto))
        print('Duas parcelas de ................R${:.2f}'.format(valor_produto / 2))
        print('Valor final da compra: ..........R${:.2f}'.format(valor_produto))
    elif pag_cartao == '3':
        print('Valor da compra ............R${:.2f}'.format(valor_produto))
        print('Juro de 20% aplicados na compra')
        print('Valor final da compra: ..........R${:.2f}'.format(juros(valor_produto)))

elif metodo_pagamento == 'x':
    print('<<COMPRA CANCELADA>>')
