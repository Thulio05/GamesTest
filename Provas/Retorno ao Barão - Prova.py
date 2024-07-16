import random

dialAbertura = ['Imediato: Mestre Cecil, a tripulação está indagando se foi certo o que fizemos ao roubar o cristal das mãos de civís.',
                'Cecil: Também não gostei do que vi, mas não cabe a nós questionar a ordem do rei',
                'Cecil: Logo chegaremos ao reino de Biron e é melhor que esses comentários cessem logo ou .....',
                'Timoneiro: Monstros na proa!',
                'Cecil: Preparem-se para a batalha.']

dialFechamento = ['Imediato: Estamos condenados.',
                  'Cecil: A cada dia que se passa, monstros cada vez mais fortes nos ameaçam.']

poções = ['atk', 'def','hp']

def inteiroAleatorio(inf, sup):
    return random.randint(inf, sup)

def importaImagem(arquivo):
    arq = open(arquivo)
    per = arq.read()
    arq.close()
    return per

def continuação(dialogo):
    print('='*120)
    print(dialogo)
    print('='*120)
    input('Enter para continuar.')

olhão = {
    'nome' : 'Olhão',
    'imagem' : 'Imagem n definida',
    'tipo' : 'monstro',
    'atk' : inteiroAleatorio(1, 20),
    'def' : inteiroAleatorio(1, 10),
    'hp' : inteiroAleatorio(1, 80),
    'ágil' : inteiroAleatorio(0, 2),
}
olhudo = {
    'nome' : 'Olhudo',
    'imagem' : 'Imagem n definida',
    'tipo' : 'monstro',
    'atk' : inteiroAleatorio(1, 20),
    'def' : inteiroAleatorio(1, 10),
    'hp' : inteiroAleatorio(1, 80),
    'ágil' : inteiroAleatorio(0, 2),
}
cecil = {
    'nome' : 'Cecil',
    'imagem' : 'Imagem n definida',
    'tipo' : 'Protagonista',
    'atk' : inteiroAleatorio(1, 20),
    'def' : inteiroAleatorio(1, 10),
    'hp' : inteiroAleatorio(1, 100),
    'ágil' : inteiroAleatorio(0, 2),
}

personagens = [olhão, olhudo, cecil]

for c in range(0,4):
    continuação(dialAbertura[c])