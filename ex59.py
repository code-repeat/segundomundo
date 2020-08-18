from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''
            ESCOLHA UMA OPERAÇÃO
            [1] somar
            [2] multiplicar
            [3] maior
            [4] novos números
            [5] sair do programa
        ''')
    opcao = input('>>> ')

    if opcao == '1':
       print(f'A soma entre {n1} e {n2} é {n1+n2}')
    elif opcao == '2':
        print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}')
    elif opcao == '3':
        if n1 > n2:
            print(f'O número {n1} é maior que o número {n2}')
        elif n2 > n1:
            print(f'O número {n2} é maior que o número {n1}')
        else:
            print('Os valores são iguais')
    elif opcao == '4':
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == '5':
        break

    else:
        print('Opção inválida! Tente novamente')
    print('=-=' * 10)
        
print('Finalizando a aplicação...')