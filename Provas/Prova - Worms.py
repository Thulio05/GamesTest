import random, math

def inteiroAleatorio(inf, sup):
    x = 0
    while x == 0:
        x = random.randint(inf, sup)
    return x

print('-='*10)
print('  VERMES DE GUERRA   ')
print('-='*10)

matriz = []
matrizcopia = []
inicio = 0

def validaçao(txt, valores):
    res = int(input(f'{txt} '))
    while res not in valores:
        res = int(input(f'ERRO DE VALIDAÇÃO! {txt}'))
    return res

def menu_inicial():
    print('\nEscolha uma das opções abaixo: \n1 - Configurar \n2 - Iniciar Partida \n0 - Sair \n')
    escolha = validaçao('O que deseja?', [0, 1, 2])
    return escolha

def vermes():
    global MaMe1, MaMe2, verme1, verme2
    nome1 = str(input('Nome do 1° Verme: '))
    verme1 = {
        'nomeV1' : nome1,
        'combustível1' : 10,
        'muniçao1' : inteiroAleatorio(10, 20),
        'ângulo1' : inteiroAleatorio(30, 120),
        'direçao1' : inteiroAleatorio(-1, 1),
        'posiçao1' : inteiroAleatorio(0, 69),
        'velocidade1' : inteiroAleatorio(0, 5),
    }
    if verme1['direçao1'] == -1:
        MaMe1 = '<'
    elif verme1['direçao1'] == +1:
        MaMe1 = '>'

    nome2 = str(input('Nome do 2° Verme: '))
    verme2 = {
        'nomeV2' : nome2,
        'combustível2' : 10,
        'muniçao2' : inteiroAleatorio(10, 20),
        'ângulo2' : inteiroAleatorio(30, 120),
        'direçao2' : inteiroAleatorio(-1, 1),
        'posiçao2' : inteiroAleatorio(0, 69),
        'velocidade2' : inteiroAleatorio(0, 5),
    }
    if verme2['direçao2'] == -1:
        MaMe2 = '<'
    elif verme2['direçao2'] == +1:
        MaMe2 = '>'

def configuraçoes(): 
    global listavelocidade, inicio
    inicio = 1
    vermes()
    listavelocidade = []
    listavelocidade.append(verme1['velocidade1'])
    listavelocidade.append(verme2['velocidade2'])
    listavelocidade.sort()
    
def jogo():
    global MaMe1, MaMe2
    while verme1['combustível1'] > 0 or verme2['combustível2'] > 0:
        while verme1['combustível1'] > 0:
            print('')
            for k, v in verme1.items():
                print(f'{k} - {v}')
            matrizsecundaria()
            matrizcopia[3][verme1['posiçao1']] = MaMe1
            matrizcopia[3][verme2['posiçao2']] = MaMe2
            print(f'\nTurno de {verme1["nomeV1"]}...')
            mostrar_matriz_copia()
            começo = menujogo()
            if começo == 1:
                mover = validaçao('Mova-se: ', [4, 6])
                if mover == 4:
                    verme1['posiçao1'] -= 1
                    MaMe1 = '<'
                elif mover == 6:
                    verme1['posiçao1'] += 1
                    MaMe1 = '>'
                verme1['combustível1'] -= 1
            elif começo == 2:
                while True:
                    print(f'Angulação: {verme1["ângulo1"]}')
                    angulaçao = validaçao('Altere a angulação', [2, 8, 0])
                    if angulaçao == 2 and angulaçao != 30:
                        verme1['ângulo1'] -= 1
                    elif angulaçao == 8 and angulaçao != 120:
                        verme1['ângulo1'] += 1
                    elif angulaçao == 0:
                        print('Angulação ajustada!')
                        break
            elif começo == 3 and verme1['muniçao1'] > 0:
                tiro = (200 * (math.sin(2*(verme1['ângulo1'])))/9.8)
                verme1['muniçao1'] -= 1
                if tiro == verme2['posiçao2']:
                    print(f'Você acertou! {verme2} perdeu 5 de combustível!')
                    verme2['combustível2'] -= 2
                else:
                    print(f'Ops, posição do seu tiro: {tiro}')
                break
            elif começo == 0:
                print(f'\nPassando o turno de {verme1["nomeV1"]}\n')
                break
        if verme1['combustível1'] <= 0:
            print(f'Comustível de {verme1["nomeV1"]} zerado ou menor que 0... você está morto! \nVitória de {verme2["nomeV2"]}')
            break
        if verme2['combustível2'] <= 0:
            print(f'Comustível de {verme2["nomeV2"]} zerado ou menor que 0... você está morto! \nVitória de {verme1["nomeV1"]}')
            break
        while verme2['combustível2'] > 0:
            print('')
            for k, v in verme2.items():
                print(f'{k} - {v}')

            matrizsecundaria()
            matrizcopia[3][verme1['posiçao1']] = MaMe1
            matrizcopia[3][verme2['posiçao2']] = MaMe2
            print(f'\nTurno de {verme2["nomeV2"]}...\n')
            mostrar_matriz_copia()
            começo = menujogo()
            if começo == 1:
                mover = validaçao('Mova-se: ', [4, 6])
                if mover == 4:
                    verme2['posiçao2'] -= 1
                    MaMe2 = '<'
                elif mover == 6:
                    verme2['posiçao2'] += 1
                    MaMe2 = '>'
                verme2['combustível2'] -= 1
            elif começo == 2:
                while True:
                    print(f'Angulação: {verme2["ângulo2"]}')
                    angulaçao = validaçao('Altere a angulação', [2, 8, 0])
                    if angulaçao == 2 and angulaçao != 30:
                        verme2['ângulo2'] -= 1
                    elif angulaçao == 8 and angulaçao != 120:
                        verme2['ângulo2'] += 1
                    elif angulaçao == 0:
                        print('Angulação ajustada!')
                        break
            elif começo == 3 and verme2['muniçao2'] > 0:
                tiro2 = verme2['posiçao2']+(200 * (math.sin(2*(verme2['ângulo2'])))/9.8)
                verme2['muniçao2'] -= 1
                if tiro2 == verme1['posiçao1']:
                    print(f'Você acertou! {verme1} perdeu 5 de combustível!')
                    verme1['combustível1'] -= 2
                else:
                    print(f'Ops, posição do seu tiro: {tiro}')
                break
            elif começo == 0:
                print(f'\nPassando o turno de {verme2["nomeV2"]}\n')
                break
        if verme1['combustível1'] <= 0:
            print(f'Comustível de {verme1["nomeV1"]} zerado ou menor que 0... você está morto! \nVitória de {verme2["nomeV2"]}')
            break
        if verme2['combustível2'] <= 0:
            print(f'Comustível de {verme2["nomeV2"]} zerado ou menor que 0... você está morto! \nVitória de {verme1["nomeV1"]}')
            break

def menujogo():
    print('\nEscolha uma das opções abaixo: \n1 - Mover \n2 - Ajustar ângulo \n3 - Disparar \n0 - Encerrar turno')
    escolha = validaçao('Sua ação: ', [0, 1, 2, 3])
    return escolha

def matrizoriginal():
    for linha in range(0,6):
        matriz.append([])
        for coluna in range(0,70):
            if linha == 4:
                matriz[linha].append('X')
            elif linha == 5:
                matriz[linha].append('X')
            else:
                matriz[linha].append('')

def matrizsecundaria():
    global matrizcopia
    matrizcopia.clear()
    for linha in range(0,6):
        matrizcopia.append([])
        for coluna in range(0,70):
            if linha == 4:
                matrizcopia[linha].append('X')
            elif linha == 5:
                matrizcopia[linha].append('X')
            else:
                matrizcopia[linha].append('')

def mostrar_matriz_copia():
    for i in matrizcopia:
        print(*i)

matrizoriginal()

while True:
    escolhainicial = menu_inicial()
    if escolhainicial == 1:
        configuraçoes()
    elif escolhainicial == 2:
        if inicio == 0:
            print('Configure os personagens antes de iniciar a partida.')
        else:
            matrizsecundaria()
            jogo()
            print('\nJogo encerrado!')
            break
    elif escolhainicial == 0:
        print('Vermes indo para terra descansar...')
        break