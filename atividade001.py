nome = 'luan'
nota1 = 10
nota2 = 10
faltas = 4
media = (nota1 + nota2) / 2

if media >= 7:
    if faltas < 3:
        print('O aluno(a)', nome, 'foi aprovado com a média:', media)
    else: print('O aluno(a)', nome, 'foi reprovado por ter', faltas, 'faltas!')
else:
    if faltas > 3:
        print('O aluno(a)', nome, 'foi aprovado com a média: ', media, 'e por ter', faltas, 'faltas!')
    else: print('O aluno(a)', nome, 'foi reprovado com a média: ', media)


