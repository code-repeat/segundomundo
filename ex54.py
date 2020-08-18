from datetime import date
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    atual = date.today().year
    nasc = int(input(f'Em que ano a {pess}º pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1 #  mais uma pessoa maior de idade
    else:
        totmenor += 1 #  menos uma pessoa menor de idade
print(f'Ao todo tivemos {totmaior} pessoa(s) maior de idade \n e {totmenor} pessoa(s) menor de idade')
