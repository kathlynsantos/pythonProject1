
candidato_x = 0
candidato_y = 0
candidato_z = 0
branco = 0
voto = 1
continuar = 1
pretencao = ' '

while continuar == 1:
    voto = input('escolha seu candidato:\nCandidato_X - 889\nCandidato_Y - 847\nCandidato_Z - 515\nBranco - 0\n')
    if voto == 889:
        Variavel = candidato_x+1
    elif voto == 847:
        Variavel = candidato_y+1
    elif voto == 515:
        Variavel = candidato_z+1
    elif voto == 0:
        Variavel = branco+1

    pretencao = input ('continuar votando? se sim digite "sim" se não digite qualquer letra e confirme: ')
    if pretencao == 'sim':
        continuar = 1
    else:
        continuar = 0
        print('O candidato Candidato_X teve', candidato_x, 'votos \nO candidato Candidato_Y teve', candidato_y, 'votos\n0 candidato Candidato_Z teve', candidato_z, 'votos\nE', branco, 'pessoas votaram Branco')




