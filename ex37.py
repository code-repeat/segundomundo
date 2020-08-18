from time import sleep
print('''
Escolha um tipo de conversão:
   [1] - para binário
   [2] - para octal
   [3] - para hexadecimal
''')

opcao = int(input('>>> '))
sleep(3)
decimal = int(input('Digite um valor em decimal (inteiro): '))

if opcao == 1:
    print('O número {} em binário é {}'.format(decimal, bin(decimal)[2:]))
elif opcao == 2:
    print('O número {} em octal é {}'.format(decimal, oct(decimal)[2:]))
elif opcao == 3:
    print('O número {} em hexadecimal é {}'.format(decimal, hex(decimal)[2:]))
else:
    print('Opção inválida. Tente novamente')
