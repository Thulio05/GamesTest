matriz = []
pontoarmador = pontoandarilho = armador = andarilho = fator = 0

def validaçao(txt, valores):
    resp = int(input(f'{txt}'))
    while resp not in valores:
        resp = int(input(f'ERRO DE ENTRADA! Escolha um número válido: '))
    return int(resp)

def menu():
    print('''Opções:
    1 - Definir Armador
    2 - Plantar Armadilhas
    3 - Iniciar com Andarilho
    4 - Mostrar o placar
    0 - Finalizar o Jogo\n''')
    resp = int(input('O q deseja fazer? '))
    return resp

def escolha_jogador():
    global armador 
    armador = int(input('Qual jogador será o Armador? '))
    while armador not in [1, 2]:
        armador = int(input('ERRO DE ENTRADA! Qual jogador será o Armador? '))
    if armador == 1:
        andarilho = 2
    else:
        andarilho = 1
    return andarilho

def mapa():
    print(f'Jogador {armador} , você pode esconder até 3 ovos podres por linha do terreno.')
    for linha in range(0,5):
        for c in range(0,3):
            mostrar_matriz()
            coluna = int(input(f'Em qual coluna da linha {linha+1} você quer esconder ovos podres? [1 a 5] '))
            while coluna not in [1, 2, 3, 4, 5]:
                coluna = int(input(f'ERRO DE ENTRADA! Em qual coluna da linha {linha+1} você quer esconder ovos podres? [1 a 5] '))
            matriz[linha][coluna-1] = 'O'
            if c != 2:
                escolha = str(input('Deseja continuar? [S/N] ')).upper()
                while escolha not in 'SN':
                    escolha = str(input('ERRO DE ENTRADA! Deseja continuar? [S/N] ')).upper()
                if escolha == 'N':
                    break
            if c == 3:
                break
    print('Este é o terreno com as armadilhas plantadas: ')
    mostrar_matriz()
    reset = str(input('Deseja refazer seu campo? [S/N] ')).upper()
    while reset not in 'SN':
        reset = str(input('ERRO NA ENTRADA! Deseja refazer seu campo? [S/N] ')).upper()
    if reset == 'S':
        criação_da_matriz()
        mapa()

def mostrar_matriz():
    print(f'''
        0 1 2 3 4 5
        1 {matriz[0][0]} {matriz[0][1]} {matriz[0][2]} {matriz[0][3]} {matriz[0][4]}
        2 {matriz[1][0]} {matriz[1][1]} {matriz[1][2]} {matriz[1][3]} {matriz[1][4]}
        3 {matriz[2][0]} {matriz[2][1]} {matriz[2][2]} {matriz[2][3]} {matriz[2][4]}
        4 {matriz[3][0]} {matriz[3][1]} {matriz[3][2]} {matriz[3][3]} {matriz[3][4]}
        5 {matriz[4][0]} {matriz[4][1]} {matriz[4][2]} {matriz[4][3]} {matriz[4][4]}\n''')

def criação_da_matriz():
    fator = 1
    global matriz
    matriz.clear()
    for linha in range(0,5):
        matriz.append([])
        for coluna in range(0,5):
            matriz[linha].append('A')

def jogar():
    global pontoarmador
    global pontoandarilho
    global escolha
    print('''São válidos os espaços: [1, 2, 3, 4, 5]
Escolha sabiamente um dos espaços válidos''')
    while True:
        escolha = int(input('Escolha: '))
        if escolha not in [1, 2, 3, 4, 5]:
            escolha = int(input('ERRO NA ENTRADA! Escolha: '))
        if matriz[0][escolha-1] == 'O':
            print('Eca! Você pisou em um ovo podre e perdeu')
            pontoarmador = pontoarmador + 1
            break
        elif matriz[0][escolha] == 'A':
            print('Passado a 1° linha!')
            print(f' [{escolha-1}], [{escolha}], [{escolha+1}]')
            print('Escolha sabiamente um dos espaços válidos')
            for c in range(2,5):
                if c == 2:
                    nova_escolha = validaçao('Escolha: ', [escolha-1, escolha, escolha+1])
                else:
                    nova_escolha = validaçao('Escolha: ', [nova_escolha-1, nova_escolha, nova_escolha+1])
                if escolha-1 == matriz[1][0]:
                    print(f' {escolha}, {escolha+1}')
                elif escolha-1 == matriz[1][4]:
                    print(f' [{escolha-1}], [{escolha}]')
                else:
                    print(f' [{nova_escolha-1}], [{nova_escolha}], [{nova_escolha+1}]')
                if matriz[c][nova_escolha] == 'O':
                    print('Eca! Você pisou em um ovo podre e perdeu')
                    pontoarmador = pontoarmador + 1
                    break
                elif matriz[c][nova_escolha] == 'A':
                    print(f'Passada a {c+1} linha')
                if c == 4 and matriz[c][nova_escolha] == 'O':
                    print('Eca! Você pisou em um ovo podre e perdeu')
                    pontoarmador = pontoarmador + 1
                    break
                elif c == 4 and matriz[c][nova_escolha] == 'A':
                    print('Parabéns! O andarilho concluiu a passagem!')
                    pontoandarilho = pontoandarilho+1
        break

while True:
    resp = menu()
    if resp == 1:
        andarilho = escolha_jogador()
        print(f'''\nO jogador armador é o {armador}
o jogador andarilho é o {andarilho}\n''')
    elif resp == 2:
        if armador == 1 or armador == 2:
            criação_da_matriz()
            mapa()
        else:
            print('OPS! Armaddor não definido. Selecione a opção 1 e tente novamente!\n')
    elif resp == 3:
        cont = 5
        for c in range(100):
            print('='*cont)
            cont += 1
        jogar()
    elif resp == 4:
        print(f'Jogador {armador} - {pontoarmador} pontos')
        print(f'Jogador {andarilho} - {pontoandarilho} pontos\n')
    elif resp == 0:
        print('Finalizando o Jogo...')
        break