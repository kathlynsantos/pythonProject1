nome = str(input('digite seu nome completo: '))
ano = int(input('digite seu ano de nascimento: '))

while 1922 < ano > 2021:
    input('digite um ano de nascimento válido\ndigite seu ano de nascimento: ')

if nome:
    if 1922 < ano > 2021:
        idade = (ano - 2022) * -1
        print(nome, 'de idade', idade)

