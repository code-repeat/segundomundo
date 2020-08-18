soma_idade = 0
mulh_menores_vinte = 0
maior_idade_h = 0
nome_homem_velho = ''
for i in range(1, 5):
    print('----- {}ª PESSOA -----'.format(i))
    nome = str(input("Pessoa: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade
    if sexo == 'F':
        if idade < 20:
            mulh_menores_vinte += 1
    elif sexo == 'M' and i == 1:
        maior_idade_h = idade
        nome_homem_velho = nome

    if sexo == 'M' and idade > maior_idade_h:
        nome_homem_velho = nome


print('A idade média do grupo é {:.2f} anos'.format(soma_idade/4))
print(f'O homem mais velho se chama {nome_homem_velho} e tem {maior_idade_h} anos')
print(f'Quantidade de mulheres menores de vinte anos: {mulh_menores_vinte}')


