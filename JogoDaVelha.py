tabuleiro = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def exibe_tabuleiro():
    print('  1   2   3')
    for i in range(len(tabuleiro)):
        print(f'{i + 1}', end='')
        for j in range(len(tabuleiro[i])):
            if j != len(tabuleiro[i]) - 1:
                if tabuleiro[i][j] == 0:
                    print(f' {" "} |', end='')
                else:
                    print(f' {tabuleiro[i][j]} |', end='')
            else:
                if tabuleiro[i][j] == 0:
                    print(f' {" "} ')
                else:
                    print(f' {tabuleiro[i][j]} ')
        if i != len(tabuleiro) - 1:
            print(' ---+---+---')


def verifica_jogada(c1, c2, jogador):
    if (c1 - 1 > 2 or c1 - 1 < 0) or (c2 - 1 > 2 or c2 - 1 < 0):
        return False
    if tabuleiro[c1 - 1][c2 - 1] == 'X' or tabuleiro[c1 - 1][c2 - 1] == 'O':
        return False
    else:
        if jogador % 2 == 1:
            tabuleiro[c1 - 1][c2 - 1] = 'X'
        else:
            tabuleiro[c1 - 1][c2 - 1] = 'O'
        return True


def verifica_vencedor():
    # Horizontal
    for x in range(3):
        if tabuleiro[x][0] == tabuleiro[x][1] == tabuleiro[x][2] and tabuleiro[x][0] == 'X':
            return 1
        elif tabuleiro[x][0] == tabuleiro[x][1] == tabuleiro[x][2] and tabuleiro[x][0] == 'O':
            return 2
    # Vertical
    for x in range(3):
        if tabuleiro[0][x] == tabuleiro[1][x] == tabuleiro[2][x] and tabuleiro[0][x] == 'X':
            return 1
        elif tabuleiro[0][x] == tabuleiro[1][x] == tabuleiro[2][x] and tabuleiro[0][x] == 'O':
            return 2
    # Diagonal principal
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] == 'X':
        return 1
    elif tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] == 'O':
        return 2
    # Diagonal secundária
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] == 'X':
        return 1
    elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] == 'O':
        return 2


def jogar():
    c = 1
    while c != 10:
        exibe_tabuleiro()
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))

        if verifica_jogada(linha, coluna, c):
            c += 1
        else:
            print('Jogada inválida, tente novamente')

        if verifica_vencedor() == 1:
            print('Jogador 1 venceu')
            break
        elif verifica_vencedor() == 2:
            print('Jogador 2 venceu')
            break

    if verifica_vencedor() is None:
        print('Empate')


jogar()